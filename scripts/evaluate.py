def score(output, expected):
    return sum(e in output for e in expected) / len(expected)
