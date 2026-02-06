from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini")

def generate_answer(context, question):
prompt = f"""
Context:
{context}

Question:
{question}
"""
return llm([HumanMessage(content=prompt)]).content
