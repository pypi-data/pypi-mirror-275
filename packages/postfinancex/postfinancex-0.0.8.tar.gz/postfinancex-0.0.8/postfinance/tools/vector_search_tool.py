import pathlib

from langchain.tools import Tool
from llama_index.core import (
    Settings,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.schema import TextNode
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.embeddings.jinaai import JinaEmbedding
from llama_index.llms.watsonx import WatsonX


def get_vector_search_tool(settings) -> Tool:

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

    Settings.llm = llm
    Settings.embed_model = embed_model

    # index
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir=str(pathlib.Path(settings.persist_dir) / "vector"),
        )
        vector_index = load_index_from_storage(storage_context)
    except Exception as e:
        print(f"Failed to load persistent index: {e}")

        from ..storage import mongo_storage_from_uri

        mongo_storage = mongo_storage_from_uri(settings.mongo_uri)

        nodes = [
            TextNode(id_=c["id"], text=c["translation"])
            for c in mongo_storage.calls
        ]

        vector_index = VectorStoreIndex(nodes)
        vector_index.storage_context.persist(
            persist_dir=str(pathlib.Path(settings.persist_dir) / "vector"),
        )

    # query engine
    vector_search_engine = vector_index.as_query_engine(similarity_top_k=3)

    # tool
    vector_search_tool = QueryEngineTool(
        vector_search_engine,
        metadata=ToolMetadata(
            name="vector_search",
            description="Useful for searching for specific information in a document that is relevant to the current question.",
        ),
    )

    return vector_search_tool.to_langchain_tool()
