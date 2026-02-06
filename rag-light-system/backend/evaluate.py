def faithfulness(answer, context):
hits = sum(1 for word in answer.split() if word in context)
return hits / max(len(answer.split()), 1)
