from dataclasses import dataclass
from typing import Optional


@dataclass
class ModelParams:

    decoding_method: Optional[str] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    temperature: Optional[float] = None
    random_seed: Optional[int] = None
    repetition_penalty: Optional[float] = None
    min_new_tokens: Optional[int] = None
    max_new_tokens: Optional[int] = None

    def to_dict(self):
        if self.random_seed == 0:
            self.random_seed = None
        return {k: v for k, v in self.__dict__.items() if v is not None}


@dataclass
class Tools:

    translate: bool = False
    graph_qa: bool = False
    vector_search: bool = False
    summarize: bool = False

    def to_list(self):
        return [k for k, v in self.__dict__.items() if v]


@dataclass
class _Settings:

    _watsonx_api_key: str = ""
    _watsonx_url: str = ""
    _watsonx_project_id: str = ""
    _watsonx_model_id: str = "meta-llama/llama-3-70b-instruct"
    _watsonx_model_params: ModelParams = ModelParams(
        decoding_method="sample",
        top_p=0.9,
        top_k=50,
        temperature=0.6,
        random_seed=0,
        repetition_penalty=1.0,
        min_new_tokens=0,
        max_new_tokens=1024,
    )
    _jina_api_key: str = ""
    _neo4j_uri: str = ""
    _neo4j_username: str = ""
    _neo4j_password: str = ""
    _mongo_uri: str = ""
    _persist_dir: str = "./storage"
    _tools: Tools = Tools(
        translate=False,
        graph_qa=True,
        vector_search=True,
        summarize=False,
    )
    _verbose: bool = False

    # llm, IBM watsonx
    @property
    def watsonx_api_key(self) -> str:
        return self._watsonx_api_key

    @watsonx_api_key.setter
    def watsonx_api_key(self, value: str) -> None:
        self._watsonx_api_key = value

    @property
    def watsonx_url(self) -> str:
        return self._watsonx_url

    @watsonx_url.setter
    def watsonx_url(self, value: str) -> None:
        self._watsonx_url = value

    @property
    def watsonx_project_id(self) -> str:
        return self._watsonx_project_id

    @watsonx_project_id.setter
    def watsonx_project_id(self, value: str) -> None:
        self._watsonx_project_id = value

    @property
    def watsonx_model_id(self) -> str:
        return self._watsonx_model_id

    @watsonx_model_id.setter
    def watsonx_model_id(self, value: str) -> None:
        self._watsonx_model_id = value

    @property
    def watsonx_model_params(self) -> ModelParams:
        return self._watsonx_model_params

    @watsonx_model_params.setter
    def watsonx_model_params(self, value: ModelParams) -> None:
        self._watsonx_model_params = value

    # embeddings, Jina Embeddings
    @property
    def jina_api_key(self) -> str:
        return self._jina_api_key

    @jina_api_key.setter
    def jina_api_key(self, value: str) -> None:
        self._jina_api_key = value

    # graph, Neo4j Aura
    @property
    def neo4j_uri(self) -> str:
        return self._neo4j_uri

    @neo4j_uri.setter
    def neo4j_uri(self, value: str) -> None:
        self._neo4j_uri = value

    @property
    def neo4j_username(self) -> str:
        return self._neo4j_username

    @neo4j_username.setter
    def neo4j_username(self, value: str) -> None:
        self._neo4j_username = value

    @property
    def neo4j_password(self) -> str:
        return self._neo4j_password

    @neo4j_password.setter
    def neo4j_password(self, value: str) -> None:
        self._neo4j_password = value

    # store, MongoDB Atlas
    @property
    def mongo_uri(self) -> str:
        return self._mongo_uri

    @mongo_uri.setter
    def mongo_uri(self, value: str) -> None:
        self._mongo_uri = value

    @property
    def tools(self) -> Tools:
        return self._tools

    @tools.setter
    def tools(self, value: Tools) -> None:
        self._tools = value

    # persist
    @property
    def persist_dir(self) -> str:
        return self._persist_dir

    @persist_dir.setter
    def persist_dir(self, value: str) -> None:
        self._persist_dir = value

    # verbose
    @property
    def verbose(self) -> bool:
        return self._verbose

    @verbose.setter
    def verbose(self, value: bool) -> None:
        self._verbose = value


# Singleton
Settings = _Settings()
