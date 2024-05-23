import threading
import yaml
import os
import os
import litellm
from langchain.cache import RedisCache
from langchain.globals import set_llm_cache
import redis

# TODO move cache setting to the config file
# We do not use LiteLLM's cache, use LangChain's instead
# litellm.enable_cache(type="redis", url="redis://localhost:6379")
redis_client = redis.Redis.from_url("redis://localhost:6379")
set_llm_cache(RedisCache(redis_client))

litellm.drop_params = (
    True  # Drops unsupported parameters for non-OpenAI APIs like TGI and Together.ai
)


all_llm_endpoints = None
prompt_dirs = None
prompt_log_file = None
prompt_logs = {}
prompts_to_skip_for_debugging = None
local_engine_set = None


def load_config_from_file(config_file: str):
    global all_llm_endpoints, prompt_dirs, prompt_log_file, prompts_to_skip_for_debugging, local_engine_set
    # TODO raise errors if these values are not set, use pydantic v2

    with open(config_file, "r") as config_file:
        config = yaml.unsafe_load(config_file)

    prompt_dirs = config.get("prompt_dirs", ["./"])
    prompt_log_file = config.get("prompt_logging", {}).get(
        "log_file", "./prompt_logs.jsonl"
    )
    prompts_to_skip_for_debugging = set(
        config.get("prompt_logging", {}).get("prompts_to_skip", [])
    )

    litellm.set_verbose = config.get("litellm_set_verbose", False)

    all_llm_endpoints = config.get("llm_endpoints", [])
    for a in all_llm_endpoints:
        if "api_key" in a:
            a["api_key"] = os.getenv(a["api_key"])

    all_llm_endpoints = [
        a
        for a in all_llm_endpoints
        if "api_key" not in a or (a["api_key"] is not None and len(a["api_key"]) > 0)
    ]  # remove resources for which we don't have a key

    # tell LiteLLM how we want to map the messages to a prompt string for these non-chat models
    for endpoint in all_llm_endpoints:
        if "prompt_format" in endpoint:
            if endpoint["prompt_format"] == "distilled":
                # {instruction}\n\n{input}\n
                for engine, model in endpoint["engine_map"].items():
                    litellm.register_prompt_template(
                        model=model,
                        roles={
                            "system": {
                                "pre_message": "",
                                "post_message": "\n\n",
                            },
                            "user": {
                                "pre_message": "",
                                "post_message": "\n",
                            },
                            "assistant": {
                                "pre_message": "",
                                "post_message": "\n",
                            },  # this will be ignored since "simple" format only supports one output turn
                        },
                        initial_prompt_value="",
                        final_prompt_value="",
                    )
            else:
                raise ValueError(
                    f"Unsupported prompt format: {endpoint['prompt_format']}"
                )
    all_configured_engines = []
    local_engine_set = set()

    for endpoint in all_llm_endpoints:
        for engine, model in endpoint["engine_map"].items():
            all_configured_engines.append(engine)
            if model.startswith("huggingface/"):
                local_engine_set.add(engine)


# this code is not safe to use with multiprocessing, only multithreading
thread_lock = threading.Lock()


total_cost = 0  # in USD


def add_to_total_cost(amount: float):
    global total_cost
    with thread_lock:
        total_cost += amount


def get_total_cost():
    global total_cost
    return total_cost


async def track_cost_callback(
    kwargs,  # kwargs to completion
    completion_response,  # response from completion
    start_time,
    end_time,  # start/end time
):
    try:
        if kwargs["cache_hit"]:
            # no cost because of caching
            # TODO this doesn't work with streaming
            return

        response_cost = 0
        # check if we have collected an entire stream response
        if "complete_streaming_response" in kwargs:
            # for tracking streaming cost we pass the "messages" and the output_text to litellm.completion_cost
            completion_response = kwargs["complete_streaming_response"]
            input_text = kwargs["messages"]
            output_text = completion_response["choices"][0]["message"]["content"]
            response_cost = litellm.completion_cost(
                model=kwargs["model"], messages=input_text, completion=output_text
            )
        elif kwargs["stream"] != True:
            # for non streaming responses
            response_cost = litellm.completion_cost(
                completion_response=completion_response
            )
        if response_cost > 0:
            add_to_total_cost(response_cost)
    except:
        pass
        # This can happen for example because of local models


# Assign the cost callback function
litellm.success_callback = [track_cost_callback]
