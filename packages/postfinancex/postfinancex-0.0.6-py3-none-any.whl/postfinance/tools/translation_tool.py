from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain_ibm import WatsonxLLM

TRANSLATION_GENERATION_PROMPT_TEMPLATE = """Translate the following text from detected language to English. Do NOT translate the text if it is already in English. Do NOT give any extra response that is not part of the translation.

Text:
{input}

Translation:
"""


def get_translation_tool(settings) -> Tool:

    # llm
    llm = WatsonxLLM(
        model_id="mistralai/mixtral-8x7b-instruct-v01",
        apikey=settings.watsonx_api_key,
        url=settings.watsonx_url,
        project_id=settings.watsonx_project_id,
        params={
            "decoding_method": "sample",
            "top_p": 1.0,
            "top_k": 50,
            "temperature": 0.0,
            # "random_seed": 42,
            "repetition_penalty": 1.0,
            "min_new_tokens": 0,
            "max_new_tokens": 1024,
        },
    )

    # prompt
    prompt = PromptTemplate.from_template(
        TRANSLATION_GENERATION_PROMPT_TEMPLATE
    )

    # chain
    chain = prompt | llm

    # tool
    def translate(text: str) -> str:
        if settings.verbose:
            return chain.invoke(
                text,
                config={"callbacks": [ConsoleCallbackHandler()]},
            )
        return chain.invoke(text)

    translation_tool = Tool.from_function(
        name="translate",
        description="Useful for translating text from one language to English.",
        func=translate,
        return_direct=True,
    )

    return translation_tool
