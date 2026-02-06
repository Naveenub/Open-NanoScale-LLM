def score(output, expected):
    return sum(k.lower() in output.lower() for k in expected) / len(expected)
