"""generative_agents.model.llm_model"""

import time
import re
import requests


class LLMModel:
    def __init__(self, config):
        self._api_key = config["api_key"]
        self._base_url = config["base_url"]
        self._model = config["model"]
        self._meta_responses = []
        self._summary = {"total": [0, 0, 0]}

        self._handle = self.setup(config)
        self._enabled = True

    def setup(self, config):
        raise NotImplementedError(
            "setup is not support for " + str(self.__class__)
        )

    def completion(
        self,
        prompt,
        retry=5,
        callback=None,
        failsafe=None,
        caller="llm_normal",
        **kwargs
    ):
        response, self._meta_responses = None, []
        self._summary.setdefault(caller, [0, 0, 0])
        last_exception = None
        
        for attempt in range(1, retry + 1):
            try:
                meta_response = self._completion(prompt, **kwargs).strip()
                self._meta_responses.append(meta_response)
                self._summary["total"][0] += 1
                self._summary[caller][0] += 1
                if callback:
                    try:
                        response = callback(meta_response)
                    except Exception as callback_error:
                        print(f"LLMModel.completion() callback error in {caller} (attempt {attempt}/{retry}): {type(callback_error).__name__}: {callback_error}")
                        print(f"Meta response was: {meta_response[:200]}")
                        response = None
                        raise  # Re-raise to trigger retry
                else:
                    response = meta_response
                    
                # Success - break out of retry loop
                if response is not None:
                    break
                    
            except Exception as e:
                last_exception = e
                error_type = type(e).__name__
                error_msg = str(e)
                
                # Check if this is a non-retryable error (e.g., authentication error)
                non_retryable_errors = (
                    "AuthenticationError", "PermissionDeniedError", 
                    "InvalidRequestError"
                )
                if any(err in error_type for err in non_retryable_errors):
                    print(f"LLMModel.completion() non-retryable error in {caller}: {error_type}: {error_msg}")
                    raise  # Don't retry for these errors
                
                # For retryable errors (timeout, network errors, rate limit, etc.)
                if attempt < retry:
                    # Use longer wait time for rate limit errors
                    if "RateLimit" in error_type or "rate_limit" in error_msg.lower():
                        wait_time = min(10 * attempt, 60)  # Longer wait for rate limits, max 60 seconds
                    else:
                        wait_time = min(5 * attempt, 30)  # Exponential backoff, max 30 seconds
                    print(f"LLMModel.completion() retryable error in {caller} (attempt {attempt}/{retry}): {error_type}: {error_msg}")
                    print(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                    response = None
                    continue
                else:
                    # Last attempt failed - all retries exhausted
                    print(f"LLMModel.completion() failed after {retry} attempts in {caller}: {error_type}: {error_msg}")
                    import traceback
                    traceback.print_exc()
                    # Raise exception to exit program as requested
                    raise Exception(f"LLM API call failed after {retry} retries in {caller}. Error: {error_type}: {error_msg}") from last_exception
        
        pos = 2 if response is None else 1
        self._summary["total"][pos] += 1
        self._summary[caller][pos] += 1
        
        # Return response if it's not None
        # Note: Empty string is a valid response, so we check for None explicitly
        if response is None:
            # This should not happen if retry logic works correctly, but handle it anyway
            if failsafe is not None:
                print(f"Warning: Using failsafe value for {caller} as last resort")
                return failsafe
            else:
                raise Exception(f"LLM API call failed in {caller} and no failsafe provided") from last_exception
        return response

    def _completion(self, prompt, **kwargs):
        raise NotImplementedError(
            "_completion is not support for " + str(self.__class__)
        )

    def is_available(self):
        return self._enabled  # and self._summary["total"][2] <= 10

    def get_summary(self):
        des = {}
        for k, v in self._summary.items():
            des[k] = "S:{},F:{}/R:{}".format(v[1], v[2], v[0])
        return {"model": self._model, "summary": des}

    def disable(self):
        self._enabled = False

    @property
    def meta_responses(self):
        return self._meta_responses


class OpenAILLMModel(LLMModel):
    def setup(self, config):
        from openai import OpenAI

        # Increase timeout to 60 seconds for better reliability
        timeout = config.get("timeout", 10)
        return OpenAI(api_key=self._api_key, 
                      base_url=self._base_url,
                      timeout=timeout)

    def _completion(self, prompt, temperature=0.5):
        messages = [{"role": "user", "content": prompt}]
        try:
            response = self._handle.chat.completions.create(
                model=self._model, messages=messages, temperature=temperature
            )
            if response and len(response.choices) > 0:
                return response.choices[0].message.content
            else:
                print(f"Warning: Empty or invalid response from OpenAI. Response: {response}")
                return ""
        except Exception as e:
            # Re-raise to be handled by the retry logic in completion()
            raise


class OllamaLLMModel(LLMModel):
    def setup(self, config):
        return None

    def ollama_chat(self, messages, temperature):
        headers = {
            "Content-Type": "application/json"
        }
        params = {
            "model": self._model,
            "messages": messages,
            "temperature": temperature,
            "stream": False,
        }

        response = requests.post(
            url=f"{self._base_url}/chat/completions",
            headers=headers,
            json=params,
            stream=False,
            timeout=10  # Set timeout to 300 seconds (5 minutes)
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def _completion(self, prompt, temperature=0.5):
        if "qwen3" in self._model and "\n/nothink" not in prompt:
            # 针对Qwen3模型禁用think，提高推理速度
            prompt += "\n/nothink"
        messages = [{"role": "user", "content": prompt}]
        try:
            response = self.ollama_chat(messages=messages, temperature=temperature)
            if response and "choices" in response and len(response["choices"]) > 0:
                ret = response["choices"][0]["message"]["content"]
                # 从输出结果中过滤掉<think>标签内的文字，以免影响后续逻辑
                return re.sub(r"<think>.*</think>", "", ret, flags=re.DOTALL)
            else:
                print(f"Warning: Empty or invalid response from LLM. Response: {response}")
                return ""
        except requests.exceptions.Timeout:
            print(f"Error: Request timeout when calling LLM")
            raise
        except requests.exceptions.RequestException as e:
            print(f"Error: Request failed when calling LLM: {e}")
            raise
        except Exception as e:
            print(f"Error: Unexpected error in _completion: {e}")
            raise


def create_llm_model(llm_config):
    """Create llm model"""

    if llm_config["provider"] == "ollama":
        return OllamaLLMModel(llm_config)

    elif llm_config["provider"] == "openai":
        return OpenAILLMModel(llm_config)
    else:
        raise NotImplementedError(
            "llm provider {} is not supported".format(llm_config["provider"])
        )
    return None


def parse_llm_output(response, patterns, mode="match_last", ignore_empty=False):
    if isinstance(patterns, str):
        patterns = [patterns]
    rets = []
    for line in response.split("\n"):
        line = line.replace("**", "").strip()
        for pattern in patterns:
            if pattern:
                matchs = re.findall(pattern, line)
            else:
                matchs = [line]
            if len(matchs) >= 1:
                rets.append(matchs[0])
                break
    if not ignore_empty:
        if not rets:
            error_msg = f"Failed to match llm output. Response: {response[:200]}, Patterns: {patterns}"
            raise AssertionError(error_msg)
    if mode == "match_first":
        return rets[0] if rets else None
    if mode == "match_last":
        return rets[-1] if rets else None
    if mode == "match_all":
        return rets
    return None
