from transformers import pipeline
from rag.retriever import get_retriever
from rag.prompt import build_prompt

pipe = pipeline(
    "text-generation",
    model="merged-model",
    device_map="auto",
    max_new_tokens=300
)

retriever = get_retriever()

def answer(question):
    docs = retriever.get_relevant_documents(question)
    context = "\n".join(d.page_content for d in docs)
    prompt = build_prompt(context, question)
    return pipe(prompt)[0]["generated_text"]

if __name__ == "__main__":
    while True:
        q = input(">> ")
        print(answer(q))
