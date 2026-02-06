import gradio as gr
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="Naveenub/OpenNanoScaleLLM",
    max_new_tokens=256,
)

def chat(prompt, history):
    out = pipe(prompt)[0]["generated_text"]
    history.append((prompt, out))
    return history, ""

with gr.Blocks(title="OpenNanoScaleLLM 🍌") as demo:
    gr.Markdown("""
    # 🍌 OpenNanoScaleLLM
    Nano-scale infra-focused LLM (open-source)
    """)

    chatbot = gr.Chatbot(height=450)
    msg = gr.Textbox(label="Ask an infra / DevOps question")
    clear = gr.Button("Clear")

    msg.submit(chat, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot)

demo.launch()
