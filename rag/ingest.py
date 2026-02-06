from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from pathlib import Path

DATA_DIR = Path("data/knowledge")
DB_DIR = "rag_index"

docs = []

for file in DATA_DIR.glob("*"):
    if file.suffix == ".pdf":
        docs.extend(PyPDFLoader(str(file)).load())
    else:
        docs.extend(TextLoader(str(file)).load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(chunks, embeddings)
db.save_local(DB_DIR)

print(f"Ingested {len(chunks)} chunks into FAISS")
