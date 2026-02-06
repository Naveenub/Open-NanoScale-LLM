from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Open-NanoScale-LLM",
    device_map="auto"
)

print(pipe("Debug this CI/CD failure:"))
