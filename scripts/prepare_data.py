import json
from pathlib import Path

SRC = Path("data/samples.jsonl")
DST = Path("data/processed/train.jsonl")
DST.parent.mkdir(parents=True, exist_ok=True)

def format_sample(s):
    return {
        "text": (
            "<|instruction|>\n" + s["instruction"] +
            "\n<|input|>\n" + s["input"] +
            "\n<|output|>\n" + s["output"]
        )
    }

with SRC.open() as f:
    samples = [json.loads(line) for line in f]

with DST.open("w") as f:
    for s in samples:
        f.write(json.dumps(format_sample(s)) + "\n")

print(f"Processed {len(samples)} samples → {DST}")
