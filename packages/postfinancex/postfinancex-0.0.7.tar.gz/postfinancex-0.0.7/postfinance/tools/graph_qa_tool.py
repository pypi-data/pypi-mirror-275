from langchain.chains import GraphCypherQAChain
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.tools import Tool
from langchain_community.graphs import Neo4jGraph
from langchain_ibm import WatsonxLLM

CYPHER_GENERATION_PROMPT_TEMPLATE = """You are an expert Neo4j developer, able to translate user questions into Cypher queries in order to answer questions relevant to the calls between the call-center employees at PostFinance and the customers.

You must convert the user's question based on the schema.

Schema:
{schema}

You should also be aware of the following:

`"type"` property of the node `"Message"` can be used to filter results. The `"type"` property can be `"question"`, `"problem"`, `"request"` or `"response"`.

Use only the provided relationship types and properties in the schema. Do NOT use any other relationship types or properties that are not provided.

Question:
{question}

Cypher Query:
"""

CYPHER_GENERATION_FEW_SHOT_EXAMPLES = [
    {
        "question": "How many recorded customer calls?",
        "cypher_query": "MATCH (c:Call) RETURN COUNT(c)",
    },
    {
        "question": "What is the most commonly used language in the recorded customer calls?",
        "cypher_query": "MATCH (c:Call) WITH c.detected_language AS language, COUNT(c) AS count ORDER BY count DESC RETURN language, count LIMIT 1",
    },
    {
        "question": "List summaries of recored customer calls.",
        "cypher_query": "MATCH (c:Call) RETURN c.summary AS Summary",
    },
    {
        "question": "List customer needs or intents are there.",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message) WHERE m.role = 'customer' RETURN c, COLLECT(DISTINCT m.content) AS CustomerNeeds",
    },
    {
        "question": "List types of customer needs or intents are there.",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message) WHERE m.role='customer' RETURN DISTINCT m.type AS type",
    },
    {
        "question": "How many recorded questions by customers?",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message) WHERE m.type = 'question' AND m.role = 'customer' RETURN COUNT(DISTINCT m) AS count",
    },
    {
        "question": "How many recorded problems by customers?",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message) WHERE m.type = 'problem' AND m.role = 'customer' RETURN COUNT(DISTINCT m) AS count",
    },
    {
        "question": "How many recoreded requests by customers?",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message) WHERE m.type = 'request' AND m.role = 'customer' RETURN COUNT(DISTINCT m) AS count",
    },
    {
        "question": "What are the most frequently asked questions by customers?",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message) WHERE m.type = 'question' AND m.role = 'customer' WITH m.content AS question, COUNT(m.content) AS count ORDER BY count DESC RETURN question, count",
    },
    {
        "question": "List recorded questions by customers together with corresponding responses by call-center employees.",
        "cypher_query": "MATCH (c:Call)-[:HAS_MESSAGE]->(m:Message {{type: 'question'}})-[:HAS_RESPONSE]->(r:Message) RETURN m.content AS question, r.content AS response",
    },
]

CYPHER_GENERATION_FEW_SHOT_PROMPT_PREFIX = """You are an expert Neo4j developer, able to translate user questions into Cypher queries in order to answer questions relevant to the calls between the call-center employees at PostFinance and the customers.

You must convert the user's question based on the schema.

Schema:
{schema}

You should also be aware of the following:

`"type"` property of the node `"Message"` can be used to filter results. The `"type"` property can be `"question"`, `"problem"`, `"request"` or `"response"`.

Use only the provided relationship types and properties in the schema. Do NOT use any other relationship types or properties that are not provided.

Below are a number of examples of questions and their corresponding Cypher queries."""

CYPHER_GENERATION_FEW_SHOT_EXAMPLE_PROMPT = """Question:
{question}

Cypher Query:
{cypher_query}"""

CYPHER_GENERATION_FEW_SHOT_PROMPT_SUFFIX = """Now, let's translate the user's question into a Cypher query. Do NOT include any other text in your response.

Question:
{question}

Cypher Query:
"""

ANSWER_GENERATION_PROMPT_TEMPLATE = """You are an expert Neo4j developer, able to translate Cypher query results into natural language in order to form human understandable answers relevant to the calls between the call-center employees at PostFinance and the customers.

The Cypher query result contains the information that you must use to construct an answer. The provided information is authoritative, you must never doubt it or try to use your internal knowledge to correct it.

Make the answer sound as a response to the question. Do NOT mention that you based the result on the given information.

Here is an example:

Question:
What is the most commonly used language in the recorded customer calls?

Cypher Query Result:
[{{'language': 'Swiss German', 'count': 9}}]

Helpful Answer:
Swiss German.

Follow this example when generating answers. If the provided information is empty, irrelevant or insufficient, just say that you don't know the answer. Do NOT include any other text in your response.

Cypher Query Result:
{context}

Question:
{question}

Helpful Answer:
"""


def get_graph_qa_tool(settings) -> Tool:

    # llm
    llm = WatsonxLLM(
        model_id=settings.watsonx_model_id,
        apikey=settings.watsonx_api_key,
        url=settings.watsonx_url,
        project_id=settings.watsonx_project_id,
        params=settings.watsonx_model_params.to_dict(),
    )

    # graph
    graph = Neo4jGraph(
        url=settings.neo4j_uri,
        username=settings.neo4j_username,
        password=settings.neo4j_password,
    )

    # prompts
    query_prompt = PromptTemplate.from_template(
        CYPHER_GENERATION_PROMPT_TEMPLATE
    )

    query_few_shot_prompt = FewShotPromptTemplate(
        examples=CYPHER_GENERATION_FEW_SHOT_EXAMPLES,
        example_prompt=PromptTemplate.from_template(
            CYPHER_GENERATION_FEW_SHOT_EXAMPLE_PROMPT
        ),
        prefix=CYPHER_GENERATION_FEW_SHOT_PROMPT_PREFIX,
        suffix=CYPHER_GENERATION_FEW_SHOT_PROMPT_SUFFIX,
        input_variables=["question", "schema"],
    )

    answer_prompt = PromptTemplate.from_template(
        ANSWER_GENERATION_PROMPT_TEMPLATE
    )

    # chain
    graph_qa_chain = GraphCypherQAChain.from_llm(
        llm,
        graph=graph,
        cypher_prompt=query_few_shot_prompt,
        qa_prompt=answer_prompt,
        verbose=settings.verbose,
    )

    # tool
    def graph_qa(question: str, max_iterations: int = 15) -> str:
        for _ in range(max_iterations):
            try:
                return graph_qa_chain.invoke(question)["result"]
            except Exception as e:
                continue

    graph_qa_tool = Tool.from_function(
        name="graph_qa",
        description="Useful for providing facts about recorded calls between call-center employees at PostFinance and customers using Cypher",
        func=graph_qa,
        return_direct=True,
    )

    return graph_qa_tool
