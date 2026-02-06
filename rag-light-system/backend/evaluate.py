def faithfulness(answer: str, context: str) -> float:
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    if not answer_words:
        return 0.0

    overlap = answer_words.intersection(context_words)
    return round(len(overlap) / len(answer_words), 3)
