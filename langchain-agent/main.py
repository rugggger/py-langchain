from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from tools.sql import run_query_tool, list_tables, describe_tables_tool

from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()
print(tables)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=(
                "You are an AI that can access a sqlite database.\n"
                f"The database has tables of: {tables}\n"
                "Do not make assumptions about what tables exist or what columns exist "
                "Instead, use the 'describe_tables' function"
            )),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools = [run_query_tool, describe_tables_tool]
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools,
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
)

agent_executor("Tell me the name and address of the user that ordered the most orders")


