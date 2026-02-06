from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from config import LLM_MODEL

llm = ChatOpenAI(
    model=LLM_MODEL,
    temperature=0.2
)

def generate_answer(context: str, question: str) -> str:
    prompt = f"""
You are a grounded assistant.
Answer strictly using the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm([HumanMessage(content=prompt)])
    return response.content
