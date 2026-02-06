def keyword_coverage(answer: str, keywords: list[str]) -> float:
    answer_l = answer.lower()
    return sum(k.lower() in answer_l for k in keywords) / len(keywords)


def groundedness(answer: str, context: str) -> float:
    answer_tokens = set(answer.lower().split())
    context_tokens = set(context.lower().split())
    overlap = answer_tokens & context_tokens
    return len(overlap) / max(len(answer_tokens), 1)


def hallucination_score(answer: str, context: str) -> float:
    # higher = worse
    grounded = groundedness(answer, context)
    return round(1.0 - grounded, 3)


def refusal_check(answer: str) -> bool:
    refusal_phrases = [
        "please provide",
        "need more information",
        "share logs",
        "confirm region"
    ]
    return any(p in answer.lower() for p in refusal_phrases)
