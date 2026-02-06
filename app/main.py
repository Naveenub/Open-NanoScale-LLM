from fastapi import FastAPI
from app.schemas import Query, Answer
from app.rag_engine import OpenNanoScaleLLMEngine

app = FastAPI(
    title="OpenNanoScaleLLM API",
    description="Nano-scale infra-focused LLM with RAG + tools",
    version="0.1.0"
)

engine = OpenNanoScaleLLMEngine()

@app.post("/query", response_model=Answer)
def query_llm(payload: Query):
    response = engine.answer(payload.question)
    return {"response": response}
