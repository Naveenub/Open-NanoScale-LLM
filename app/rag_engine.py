from transformers import pipeline
from rag.retriever import get_retriever
from rag.prompt import build_prompt
from tools.aws import requires_aws_context, aws_missing_info
from tools.logs import requires_logs, request_logs
from tools.api import requires_api_info, request_api_details

class OpenNanoBananaEngine:
    def __init__(self):
        self.pipe = pipeline(
            "text-generation",
            model="merged-model",
            device_map="auto",
            max_new_tokens=300
        )
        self.retriever = get_retriever()

    def precheck(self, question: str):
        if requires_aws_context(question):
            return aws_missing_info()
        if requires_logs(question):
            return request_logs()
        if requires_api_info(question):
            return request_api_details()
        return None

    def answer(self, question: str):
        msg = self.precheck(question)
        if msg:
            return msg

        docs = self.retriever.get_relevant_documents(question)
        context = "\n".join(d.page_content for d in docs)

        prompt = build_prompt(context, question)
        output = self.pipe(prompt)[0]["generated_text"]

        return output.split("Answer:")[-1].strip()
