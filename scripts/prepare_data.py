import json

def format_sample(i, inp, out):
    return {
        "text": f"<|instruction|>{i}<|input|>{inp}<|output|>{out}"
    }

with open("data/samples.jsonl") as f:
    samples = [json.loads(l) for l in f]

processed = [format_sample(s["instruction"], s["input"], s["output"]) for s in samples]

with open("data/processed/train.jsonl", "w") as f:
    for p in processed:
        f.write(json.dumps(p) + "\n")
