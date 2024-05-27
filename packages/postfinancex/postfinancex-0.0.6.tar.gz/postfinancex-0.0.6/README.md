# PostFinanceX

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

**PostFinanceX** is a Python library allows you to chat with PostFinance LLM agent powered by IBM watsonx.ai



## Installation

```bash
pip install postfinancex
```



## Quickstart

```python
from postfinance import Settings, get_agent_executor, chat

Settings.watsonx_api_key = "watsonx_api_key"
Settings.watsonx_url = "watsonx_url"
Settings.watsonx_project_id = "watsonx_project_id"
Settings.jina_api_key = "jina_api_key"
Settings.neo4j_url = "neo4j_url"
Settings.neo4j_username = "neo4j_username"
Settings.neo4j_password = "neo4j_password"
Settings.mongo_uri = "mongo_uri"
Settings.verbose = True

agent_executor = get_agent_executor()

chat(agent_executor, "What is the most commonly used language in the recorded customer calls?")
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