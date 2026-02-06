from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="merged-model",
    device_map="auto",
    max_new_tokens=256
)

prompt = "Debug this CI/CD failure: pipeline fails during docker build"
out = pipe(prompt)[0]["generated_text"]
print(out)
