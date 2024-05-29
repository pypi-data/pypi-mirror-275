# PostFinanceX

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

**PostFinanceX** is a Python library allows you to chat with PostFinance LLM agent powered by IBM watsonx.ai



## Installation

***Note: currently, only support Python 3.10  due to the ` dataclasses` module changes in the newer version***

```bash
pip install postfinancex
```



## Quickstart

Global settings

```python
from postfinance import Settings

Settings.watsonx_api_key = "watsonx_api_key"
Settings.watsonx_url = "watsonx_url"
Settings.watsonx_project_id = "watsonx_project_id"
Settings.jina_api_key = "jina_api_key"
Settings.neo4j_url = "neo4j_url"
Settings.neo4j_username = "neo4j_username"
Settings.neo4j_password = "neo4j_password"
Settings.mongo_uri = "mongo_uri"
Settings.verbose = True
```

Let's chat

```python
from postfinance import get_agent_executor, chat

agent = get_agent_executor()

chat(agent, "What is the most commonly used language in the recorded customer calls?")
```



## Get Inspired

Check out our PostFinanceX app.

[![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/imyizhang/postfinancex) [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://postfinance.streamlit.app/)



## Documentation

### `postfinance.Settings`



### `postfinance.get_agent_executor`

```
postfinance.get_agent_executor()
```



### `postfinance.StreamlitCallbackHandler`

```python
postfinance.StreamlitCallbackHandler()
```



### `postfinance.chat`

```
postfinance.chat(agent_executor, message, streamlit_callback=None)
```



### `postfinance.get_annotator`

```python
postfinance.get_annotator()
```



### `postfinance.annotate`

```python
postfinance.translate(translator, transcript, params=None, dumps=False)
```



### `postfinance.get_translator`

```python
postfinance.get_translator()
```



### `postfinance.translate`

```python
postfinance.translate(translator, transcript, params=None, dumps=False)
```



### `postfinance.mongo_storage_from_uri`

```python
postfinance.mongo_storage_from_uri(uri)
```



## License

**PostFinanceX** has a BSD-3-Clause license, as found in the [LICENSE](https://github.com/imyizhang/postfinancex/blob/main/LICENSE) file.



## Contributing

Thanks for your interest in contributing to **PostFinanceX**! Please feel free to create a pull request.



## Changelog



[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/imyizhang/postfinancex



[pypi_badge]: https://badgen.net/pypi/v/postfinancex?icon=pypi&color=black&label
[pypi_link]: https://www.pypi.org/project/postfinancex