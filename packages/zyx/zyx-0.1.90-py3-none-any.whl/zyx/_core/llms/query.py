# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# zyx is open source
# use it however you want :)
#
# 2024 Hammad Saeed
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<

import instructor
from litellm import batch_completion_models_all_responses, completion as litellm_completion
import zyx._core._core as core

def query(
        messages: core.Union[str, list[dict[str, str]]] = None,
        model: core.Optional[core.Union[str, list]] = "openai/gpt-3.5-turbo",
        api_key: core.Optional[str] = None,
        response_model : core.Optional[core.BaseModel] = None,
        debug: core.Optional[bool] = False,
        *args, **kwargs
) -> core.Union[str, list[str]]:
    """
    Complete the provided messages using the specified model and API key.
    Handles both single and multiple model scenarios. Uses the LiteLLM API.

    Example:
        ```python
        response = completion("Hi")
        print(response)
        ```

    Args:
        messages (Union[str, list[dict[str, str]]]): The messages to complete.
        model (Optional[Union[str, list]]): The model to use for completion.
        api_key (Optional[str]): The API key to use for completion.
        *args: Additional arguments.
        **kwargs: Additional keyword arguments.

    Returns:
        Union[str, list[str]]: The completion response(s).
    """
    # Preconditions
    if messages is None:
        core.logger.error(
            "Messages are required! Provide either a simple query like 'Hi how are you?' "
            "or a list of dictionaries with keys like [{'role': 'user', 'content': 'Hi how are you?'}]."
        )
        return
    
    if model is None:
        core.logger.warning("No model specified. Defaulting to 'openai/gpt-3.5-turbo'.")
        model = "openai/gpt-3.5-turbo"

    if response_model:
        if debug:
            core.logger.info("Response model provided. Using Pydantic Output.")
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        try:
            client = instructor.from_litellm(litellm_completion)
            response = client.chat.completions.create(
                messages = messages,
                model = model,
                api_key = api_key,
                response_model = response_model,
                *args, **kwargs
            )
        except Exception as e:
            core.logger.error(f"Error during the completion process: {e}")
            return
        if response:
            assert isinstance(response, response_model)
            return response
        
    if isinstance(model, list):
        # Handling a list of models
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        try:
            completions = batch_completion_models_all_responses(
                messages=messages,
                models=model,
                api_key=api_key,
                *args, **kwargs
            )
        except Exception as e:
            core.logger.error(f"Error during the batch completion process: {e}")
            return
        
        responses = []
        for response in completions:
            responses.append(response.choices[0].message.content)
        return responses
    
    else:
        # Handling a single model
        if isinstance(messages, str):
            messages = [{"role": "user", "content": messages}]
        try:
            response = litellm_completion(
                messages=messages,
                model=model,
                api_key=api_key,
                *args, **kwargs
            )
        except Exception as e:
            core.logger.error(f"Error during the completion process: {e}")
            return
        return response.choices[0].message.content

if __name__ == "__main__":
    response = query("Hi", model=["openai/gpt-3.5-turbo", "openai/gpt-3.5-turbo"])
    print(response)

    class Response(core.BaseModel):
        explanation: str
        code: str

    response = query("write me a python script for recording the current time", model="openai/gpt-3.5-turbo", response_model=Response)

    print(response)