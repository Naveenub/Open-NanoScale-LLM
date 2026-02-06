from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from config import VECTOR_DB_PATH


def retrieve(query):
db = Chroma(
persist_directory=VECTOR_DB_PATH,
embedding_function=OpenAIEmbeddings()
)
return db.similarity_search(query, k=5)
