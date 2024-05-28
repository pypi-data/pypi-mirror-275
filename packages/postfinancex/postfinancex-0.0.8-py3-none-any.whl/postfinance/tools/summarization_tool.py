import pathlib

from langchain.tools import Tool
from llama_index.core import (
    Settings,
    StorageContext,
    SummaryIndex,
    load_index_from_storage,
)
from llama_index.core.schema import TextNode
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.jinaai import JinaEmbedding
from llama_index.llms.watsonx import WatsonX


def get_summarization_tool(settings) -> Tool:

    # llm
    llm = WatsonX(
        model_id=settings.watsonx_model_id,
        credentials={
            "apikey": settings.watsonx_api_key,
            "url": settings.watsonx_url,
        },
        project_id=settings.watsonx_project_id,
        additional_kwargs=settings.watsonx_model_params.to_dict(),
    )

    # embedding model
    embed_model = JinaEmbedding(
        api_key=settings.jina_api_key,
        model="jina-embeddings-v2-base-en",
    )

    # settings
    Settings.llm = llm
    Settings.embed_model = embed_model

    # index
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir=str(pathlib.Path(settings.persist_dir) / "summary"),
        )
        summary_index = load_index_from_storage(storage_context)
    except Exception as e:
        print(f"Failed to load persistent index: {e}")

        from ..storage import mongo_storage_from_uri

        mongo_storage = mongo_storage_from_uri(settings.mongo_uri)

        nodes = [
            TextNode(id_=c["id"], text=c["translation"])
            for c in mongo_storage.calls
        ]

        summary_index = SummaryIndex(nodes)
        summary_index.storage_context.persist(
            persist_dir=str(pathlib.Path(settings.persist_dir) / "summary"),
        )

    # query engine
    summarization_engine = summary_index.as_query_engine(
        response_mode="tree_summarize",
    )

    # tool
    summarization_tool = QueryEngineTool(
        summarization_engine,
        metadata=ToolMetadata(
            name="summarize",
            description="Useful for condensing a large amount of documents into a short summary relevant to the current question.",
        ),
    )

    return summarization_tool.to_langchain_tool()
