import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from config import VECTOR_DB_PATH, EMBEDDING_MODEL

def ingest_pdf(path: str):
    doc = fitz.open(path)
    text = ""

    for page in doc:
        text += page.get_text()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_text(text)

    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=OpenAIEmbeddings(model=EMBEDDING_MODEL),
        persist_directory=VECTOR_DB_PATH
    )

    vectordb.persist()
    return len(chunks)
