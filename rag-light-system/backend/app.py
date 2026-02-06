from fastapi import FastAPI, UploadFile, File
from ingest import ingest_pdf
from retriever import retrieve
from llm import generate_answer
from evaluate import faithfulness

app = FastAPI(title="🔭 RAG Light System")

@app.post("/ingest")
async def ingest(file: UploadFile = File(...)):
    path = f"data/{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    chunks = ingest_pdf(path)

    return {
        "status": "ingested",
        "chunks_created": chunks
    }

@app.get("/ask")
def ask(q: str):
    docs = retrieve(q)
    context = "\n".join(d.page_content for d in docs)

    answer = generate_answer(context, q)
    score = faithfulness(answer, context)

    return {
        "question": q,
        "answer": answer,
        "faithfulness_score": score
    }
