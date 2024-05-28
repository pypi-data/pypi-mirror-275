from langchain.agents import AgentExecutor, create_react_agent
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_ibm import WatsonxLLM

from .settings import Settings
from .tools.graph_qa_tool import get_graph_qa_tool
from .tools.summarization_tool import get_summarization_tool
from .tools.translation_tool import get_translation_tool
from .tools.vector_search_tool import get_vector_search_tool

REACT_AGENT_PROMPT_TEMPLATE = """You are a call-center employee at PostFinance, able to have normal interactions with the customer.

Be as helpful as possible and return as much information as possible.

But, do NOT answer any questions using your pre-trained knowledge, only use the information provided in the context. If the provided context is irrelevant or insufficient, just say that you don't know the answer, you need to check with your colleagues.

TOOLS:
------

You have access to the following tools:

{tools}

You must use one of tools above to answer the question.

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}
"""


def get_agent_executor(settings=Settings) -> AgentExecutor:

    # llm
    llm = WatsonxLLM(
        model_id=settings.watsonx_model_id,
        apikey=settings.watsonx_api_key,
        url=settings.watsonx_url,
        project_id=settings.watsonx_project_id,
        params=settings.watsonx_model_params.to_dict(),
    )

    if settings.verbose:
        import json

        llm_params = json.dumps(llm.params, indent=4, ensure_ascii=False)
        print(f"Model parameters:\n{llm_params}")

    # tools
    _tools = {
        "translate": get_translation_tool(settings),
        "graph_qa": get_graph_qa_tool(settings),
        "vector_search": get_vector_search_tool(settings),
        "summarize": get_summarization_tool(settings),
    }

    tool_names = settings.tools.to_list()

    tools = [_tools[t] for t in tool_names]

    if settings.verbose:
        tool_names = ", ".join(tool_names)
        print(f"Tools:\n{tool_names}")

    # memory
    memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        k=5,
        return_messages=True,
    )

    # prompt
    prompt = PromptTemplate.from_template(REACT_AGENT_PROMPT_TEMPLATE)

    # agent
    agent = create_react_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        handle_parsing_errors=True,
        verbose=settings.verbose,
    )

    return agent_executor


def chat(agent_executor: AgentExecutor, message: str) -> str:
    return agent_executor.invoke({"input": message})["output"]
