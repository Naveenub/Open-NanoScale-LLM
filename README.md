# 🍌 OpenNanoScaleLLM

**OpenNanoScaleLLM** is a clean‑room, open‑source **nano‑scale Large Language Model (LLM)** inspired by the *ideas* behind Google’s internal small‑model research — but built **entirely in the open**, using Hugging Face Transformers.

It is designed to be **small, fast, infra‑aware, tool‑aware, and explainable**, not just fluent.

> This is not a toy fine‑tune. It is a full, end‑to‑end LLM system with training, RAG, tools, evaluation, and live demos.

---

## 🚀 Why OpenNanoScaleLLM Exists

There is **no open‑source Google NanoBanana**:

* No public repo
* No weights
* No training code

That creates a gap.

**OpenNanoScaleLLM fills that gap** with:

* A real nano‑LLM (≈1.5B params)
* Infrastructure & DevOps specialization
* Retrieval‑Augmented Generation (RAG)
* Tool‑aware reasoning to prevent hallucinations
* Transparent evaluation metrics

All built in a **clean‑room**, reproducible way.

---

## 🧠 Core Design Goals

* 🧩 **Nano‑scale** – runs on modest GPUs / CPU when quantized
* ⚡ **Fast inference** – LoRA + efficient base model
* 🎯 **Domain‑specialized** – cloud, DevOps, Linux, APIs
* 🔍 **Grounded answers** – RAG + context checks
* 🛠️ **Tool‑aware** – asks for logs, regions, APIs when needed
* 🔓 **Fully open** – Apache‑2.0 license

---

## 📐 Model Overview

| Attribute      | Value                     |
| -------------- | ------------------------- |
| Base model     | Qwen2.5-1.5B            |
| Parameters     | ~1.5B                     |
| Fine‑tuning    | LoRA (SFT)                |
| Context length | 4k tokens                 |
| License        | Apache‑2.0                |
| Library        | Hugging Face Transformers |

---

## 🏗️ Repository Structure

```text
Open-NanoScale-LLM/
├── README.md
├── LICENSE
├── requirements.txt
├── configs/
│   ├── model.yaml
│   ├── training.yaml
│   └── lora.yaml
├── data/
│   ├── raw/
│   │   ├── devops_notes.md
│   │   ├── docker_errors.md
│   │   └── k8s_troubleshooting.md
│   ├── processed/
│   │   ├── instructions.jsonl
│   │   ├── rag_chunks.jsonl
│   │   └── README.md
│   └── samples.jsonl
├── scripts/
│   ├── prepare_data.py
│   ├── train_lora.py
│   ├── merge_lora.py
│   ├── inference.py
│   └── evaluate.py
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   ├── prompt.py
│   └── qa.py
├── tools/
│   ├── aws.py
│   ├── logs.py
│   └── api.py
├── app/
│   ├── main.py
│   ├── rag_engine.py
│   └── schemas.py
├── ui/
│   └── gradio_app.py
├── evals/
│   ├── test_cases.json
│   ├── metrics.py
│   └── run_eval.py
└── dashboard/
    └── gradio_eval.py
```

---

## 🧱 ASCII Architecture Diagram (README-friendly)

This works perfectly in `README.md` and GitHub renders it cleanly.

```text
                         ┌───────────────────────────┐
                         │        User / Client       │
                         │  (CLI, Gradio, FastAPI)    │
                         └─────────────┬─────────────┘
                                       │
                                       ▼
                         ┌───────────────────────────┐
                         │   OpenNanoScaleLLM Engine │
                         │  (Inference Orchestrator) │
                         └─────────────┬─────────────┘
                                       │
               ┌───────────────────────┼───────────────────────┐
               │                       │                       │
               ▼                       ▼                       ▼
     ┌─────────────────┐   ┌─────────────────────┐   ┌─────────────────┐
     │ Tool Prechecks  │   │   RAG Retriever     │   │  Prompt Builder │
     │ (AWS / Logs /   │   │ (FAISS / Chroma)    │   │  System + Rules │
     │  API Context)   │   └───────────┬─────────┘   └──────────┬──────┘
     └────────┬────────┘               │                        │
              │                        ▼                        │
              │           ┌────────────────────────┐            │
              │           │   Vector Embeddings    │            │
              │           │ (MiniLM / SBERT)       │            │
              │           └───────────┬────────────┘            │
              │                       │                         │
              └───────────────────────┼─────────────────────────┘
                                      ▼
                         ┌───────────────────────────┐
                         │  OpenNanoBanana LLM       │
                         │ (TinyLlama + LoRA)        │
                         └─────────────┬─────────────┘
                                       │
                                       ▼
                         ┌───────────────────────────┐
                         │      Final Response        │
                         │  (Grounded + Tool-aware)  │
                         └───────────────────────────┘
```

---

## 🎨 SVG Architecture Diagram (for blog / HF / portfolio)

```svg
<svg width="900" height="620" xmlns="http://www.w3.org/2000/svg">
  <style>
    .box { fill:#f9fafb; stroke:#111827; stroke-width:1.5; rx:8; ry:8; }
    .text { font-family:Arial, sans-serif; font-size:13px; fill:#111827; }
    .arrow { stroke:#111827; stroke-width:1.4; marker-end:url(#arrowhead); }
  </style>

  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7"
      refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#111827"/>
    </marker>
  </defs>

  <!-- User -->
  <rect x="350" y="20" width="200" height="50" class="box"/>
  <text x="390" y="50" class="text">User / Client</text>

  <!-- Engine -->
  <rect x="320" y="100" width="260" height="60" class="box"/>
  <text x="350" y="135" class="text">OpenNanoBanana Engine</text>

  <!-- Tools -->
  <rect x="60" y="220" width="220" height="60" class="box"/>
  <text x="85" y="255" class="text">Tool Prechecks (AWS / Logs / API)</text>

  <!-- RAG -->
  <rect x="340" y="220" width="220" height="60" class="box"/>
  <text x="375" y="255" class="text">RAG Retriever</text>

  <!-- Prompt -->
  <rect x="620" y="220" width="220" height="60" class="box"/>
  <text x="650" y="255" class="text">Prompt Builder</text>

  <!-- LLM -->
  <rect x="320" y="350" width="260" height="60" class="box"/>
  <text x="345" y="385" class="text">TinyLlama + LoRA (LLM)</text>

  <!-- Output -->
  <rect x="350" y="460" width="200" height="50" class="box"/>
  <text x="385" y="490" class="text">Final Answer</text>

  <!-- Arrows -->
  <line x1="450" y1="70" x2="450" y2="100" class="arrow"/>
  <line x1="450" y1="160" x2="170" y2="220" class="arrow"/>
  <line x1="450" y1="160" x2="450" y2="220" class="arrow"/>
  <line x1="450" y1="160" x2="730" y2="220" class="arrow"/>
  <line x1="170" y1="280" x2="450" y2="350" class="arrow"/>
  <line x1="450" y1="280" x2="450" y2="350" class="arrow"/>
  <line x1="730" y1="280" x2="450" y2="350" class="arrow"/>
  <line x1="450" y1="410" x2="450" y2="460" class="arrow"/>
</svg>

```

---

## 🧪 Training Pipeline

### 1️⃣ Dataset

Instruction‑style JSONL focused on **infra reasoning**:

* AWS IAM, EC2, S3, ECR
* Docker & Kubernetes
* CI/CD failures
* API debugging

Example:

```json
{
  "instruction": "Why does an EC2 instance fail to access S3?",
  "input": "AccessDenied error",
  "output": "The EC2 instance likely lacks an IAM role or the attached policy does not allow s3:GetObject..."
}
```

---

### 2️⃣ Data Preparation

```bash
python scripts/prepare_data.py
```

Formats data into a model‑friendly instruction template.

---

### 3️⃣ LoRA Fine‑Tuning

```bash
python scripts/train_lora.py
```

* Efficient
* Low VRAM
* Domain‑focused

---

### 4️⃣ Merge LoRA

```bash
python scripts/merge_lora.py
```

Produces a standalone model for inference & upload.

---

## 🔍 Retrieval‑Augmented Generation (RAG)

OpenNanoBanana is **RAG‑first**, not RAG‑bolted‑on.

### RAG Flow

```
User Question
   ↓
Pre‑check (tools)
   ↓
Vector Retrieval (FAISS)
   ↓
Context Assembly
   ↓
Prompt Injection
   ↓
LLM Answer
```

### Knowledge Sources

* Markdown / PDF docs
* Cloud & DevOps references
* User‑supplied documents

Ingest once:

```bash
python rag/ingest.py
```

Run interactive QA:

```bash
python rag/qa.py
```

---

## 🛠️ Tool‑Aware Reasoning (Anti‑Hallucination)

Instead of guessing, the model **asks for missing info**.

### Built‑in Tool Signals

* **AWS** → asks for region, account, service
* **Logs** → requests error logs
* **API** → asks for endpoint, auth, method

Example:

> **User:** EC2 cannot pull image from ECR
> **Model:** Please confirm the AWS region and ensure the EC2 IAM role has `ecr:GetAuthorizationToken` permission.

This is intentional and by design.

---

## 📊 Evaluation & Hallucination Metrics

Most projects skip this. OpenNanoBanana doesn’t.

### Metrics Implemented

* **Keyword Coverage** – expected technical concepts
* **Groundedness** – answer vs retrieved context
* **Hallucination Score** – unsupported content
* **Refusal Correctness** – asks for info instead of guessing

Run batch evaluation:

```bash
python evals/run_eval.py
```

### Visual Dashboard

```bash
python dashboard/gradio_eval.py
```

Shows:

* Per‑question scores
* Hallucination trends
* Grounding quality

---

## 🌐 Live Demo

### Backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

### Frontend (Gradio)

```bash
python ui/gradio_app.py
```

A real, production‑style LLM demo — not a notebook.

---

## 🤗 Hugging Face Release

* **Model**: `hf.co/<Naveenub>/Open-NanoScale-LLM`
* **Live Space**: `hf.co/spaces/<Naveenub>/Open-NanoScale-LLM-demo`

Includes:

* Model card
* License
* Demo UI

---

## ⚖️ License

Apache License 2.0

You are free to:

* Use commercially
* Modify
* Redistribute

---

## ⚠️ Disclaimer

This project is a **clean‑room, independent open‑source implementation**.

* Not affiliated with Google
* Not derived from any proprietary NanoBanana system
* No private or restricted data used

---

## 🎯 Who This Is For

* LLM / AI Engineers
* Infra & DevOps Engineers exploring AI
* Researchers interested in small‑model systems
* Anyone tired of hype‑only LLM repos

---

## 🛣️ Roadmap

* Multi‑knowledge‑base RAG
* GGUF / Ollama packaging
* Tool execution (not just awareness)
* Deterministic infra mode

---

## ⭐ Final Note

OpenNanoBanana is meant to be:

* Readable
* Reproducible
* Honest
* Useful

If you build on it — ship it. 🍌🚀
