from dotenv import load_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent
from langchain.tools import tool
from langchain.agents import AgentExecutor
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet 
    Args: 
        query: The query to search for.
    Returns:
        The search results.
    """
    print(f"searching fro {query}")
    return "Tokyo weather is sunny"

llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
tools = [search]
prompt = ChatPromptTemplate.from_template(
    """
    Answer the following questions as best you can.

You have access to the following tools:

{tools}

Use this format:

Question: the input question
Thought: think about what to do
Action: one of [{tool_names}]
Action Input: input to the action
Observation: result of the action
...
Thought: I now know the answer
Final Answer: the answer

Question: {input}
Thought:{agent_scratchpad}
    """
)
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
def main():
    print("Hello from langchain-course!")
    result = agent_executor.invoke({"input":"what is the weather in Tokyo?"})
    print(result)
    
if __name__ == "__main__":
    main()
