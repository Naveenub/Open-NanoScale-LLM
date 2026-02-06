from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import VECTOR_DB_PATH, EMBEDDING_MODEL

def retrieve(query: str, k: int = 5):
    db = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL)
    )

    return db.similarity_search(query, k=k)
