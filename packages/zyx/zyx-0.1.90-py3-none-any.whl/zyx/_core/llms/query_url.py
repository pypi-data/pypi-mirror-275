# >>>>>>>>>>>>>>>>>>>>>>>>>>>
# zyx is open source
# use it however you want :)
#
# 2024 Hammad Saeed
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<

from llama_index.core import SummaryIndex
from llama_index.llms.litellm import LiteLLM
from llama_index.readers.web import BeautifulSoupWebReader, SimpleWebPageReader
from zyx._core.llms.query import query
import zyx._core._core as core

def query_url(
    prompt: core.Optional[str] = None,
    url: core.Optional[str] = None,
    model : core.Optional[str] = "openai/gpt-3.5-turbo",
    api_key : core.Optional[str] = None,
    response_model : core.Optional[core.BaseModel] = None,
    debug : core.Optional[bool] = False,
    *args, **kwargs
) -> core.Union[str, list[str]]:
    
    """A function to query a url with a prompt.

    Example:
        ```python
        response = query_url(prompt = "what is the title of the repository?",
                             url = "github.com/BerriAI/litellm",
                                response_model = TitleModel,
                                debug = True)
        print(response)
        ```

    Args:
        prompt (Optional[str]): The prompt to query.
        url (Optional[str]): The url to query.
        model (Optional[str]): The model to use for completion. Defaults to "openai/gpt-3.5-turbo".
        api_key (Optional[str]): The API key to use for completion.
        response_model (Optional[BaseModel]): The response model to use for completion.
        debug (Optional[bool]): Whether to print debug information. Defaults to False.
        *args: Additional arguments.
        **kwargs: Additional keyword arguments.

    Returns:
        Union[str, list[str]]: The completion response(s).
    """

    # [PRE]

    # [FUNC]
    try:
        llm = LiteLLM(model = model, api_key = api_key, temperature = 0.1)
        if response_model:
            reader = SimpleWebPageReader(html_to_text = True)
        else:
            reader = BeautifulSoupWebReader()
    except BaseException as e:
        raise core.logger.error(e)
    try:
        if debug:
            core.logger.info(f"Querying {url} with prompt: {prompt}")
        documents = reader.load_data([url])
        index = SummaryIndex.from_documents(documents)
    except BaseException as e:
        raise core.logger.error(e) from e
    try:
        query_engine = index.as_query_engine(llm)
        generation = query_engine.query(prompt)
    except BaseException as e:
        raise core.logger.error(e) from e
    
    if response_model:
        generation = generation.response
        prompt = f"""
Here is the result of a query submitted by a user: 
{generation}

Please extract the user's defined requirements according to their query:
{prompt}
"""
        try:
            response = query(messages = prompt,
                             model = model,
                             response_model = response_model,
                             api_key = api_key,
                                *args, **kwargs)   
        except BaseException as e:
            raise core.logger.error(e) from e
        
    # [POST]
        
    if response_model is None:
        response = generation.response
    
    return response

if __name__ == "__main__":

    class TitleModel(core.BaseModel):
        repo_title : str

    response = query_url(prompt = "what is the title of the repository?",
                         url = "https://github.com/BerriAI/litellm",
                         response_model = TitleModel,
                         debug = True)
    
    print(response)