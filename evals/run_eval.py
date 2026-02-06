import json
from app.rag_engine import OpenNanoScaleLLMEngine
from evals.metrics import (
    keyword_coverage,
    groundedness,
    hallucination_score,
    refusal_check
)

engine = OpenNanoScaleLLMEngine()

with open("evals/test_cases.json") as f:
    cases = json.load(f)

results = []

for case in cases:
    docs = engine.retriever.get_relevant_documents(case["question"])
    context = "\n".join(d.page_content for d in docs)
    answer = engine.answer(case["question"])

    result = {
        "question": case["question"],
        "answer": answer,
        "coverage": keyword_coverage(answer, case["expected_keywords"]),
        "groundedness": groundedness(answer, context),
        "hallucination": hallucination_score(answer, context),
        "refusal": refusal_check(answer)
    }

    results.append(result)

print(json.dumps(results, indent=2))
