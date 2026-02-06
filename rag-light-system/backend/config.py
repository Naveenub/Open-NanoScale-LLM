import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VECTOR_DB_PATH = "./data/chroma"
EMBEDDING_MODEL = "text-embedding-3-large"
LLM_MODEL = "gpt-4o-mini"
