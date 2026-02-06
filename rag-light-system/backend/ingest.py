import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from config import VECTOR_DB_PATH


def ingest_pdf(path):
doc = fitz.open(path)
text = "".join(page.get_text() for page in doc)


splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
chunks = splitter.split_text(text)


vectordb = Chroma.from_texts(
chunks,
OpenAIEmbeddings(),
persist_directory=VECTOR_DB_PATH
)
vectordb.persist()
