import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/query"

def chat(question, history):
    res = requests.post(API_URL, json={"question": question})
    answer = res.json()["response"]
    history.append((question, answer))
    return history, ""

with gr.Blocks(title="OpenNanoScaleLLM 🍌") as demo:
    gr.Markdown("""
    # 🍌 OpenNanoScaleLLM
    **Nano-scale infrastructure LLM with RAG + tool-aware reasoning**
    """)

    chatbot = gr.Chatbot(height=450)
    msg = gr.Textbox(
        placeholder="Ask an infra / cloud / DevOps question…",
        label="Your Question"
    )
    clear = gr.Button("Clear")

    msg.submit(chat, [msg, chatbot], [chatbot, msg])
    clear.click(lambda: [], None, chatbot)

demo.launch()
