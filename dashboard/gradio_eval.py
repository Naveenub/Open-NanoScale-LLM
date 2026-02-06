import gradio as gr
import json
from evals.run_eval import results

def render():
    rows = []
    for r in results:
        rows.append([
            r["question"],
            round(r["coverage"], 2),
            round(r["groundedness"], 2),
            round(r["hallucination"], 2),
            "✅" if r["refusal"] else "❌"
        ])
    return rows

with gr.Blocks(title="OpenNanoScaleLLM Evaluation Dashboard") as demo:
    gr.Markdown("""
    # 📊 OpenNanoScaleLLM Evaluation Dashboard

    **Metrics**
    - Coverage: expected technical concepts
    - Groundedness: answer-context overlap
    - Hallucination: unsupported content (lower is better)
    - Refusal: asks for missing info when required
    """)

    table = gr.Dataframe(
        headers=[
            "Question",
            "Coverage",
            "Groundedness",
            "Hallucination",
            "Refusal"
        ],
        datatype=["str", "number", "number", "number", "str"]
    )

    btn = gr.Button("Run Evaluation")
    btn.click(fn=render, outputs=table)

demo.launch()
