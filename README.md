# Open-NanoScale-LLM 🍌

OpenNanoScaleLLM is an open-source nano-scale language model optimized for
infrastructure, cloud, and systems reasoning.

## Features
- 1.1B parameter base (Qwen2.5-1.5B)
- LoRA fine-tuning
- Infra & DevOps focused
- CPU/GPU friendly
- Fully open-source

## Training
```bash
python scripts/prepare_data.py
python scripts/train_lora.py
```

Inference
```bash
python scripts/inference.py
```

Disclaimer

This project is a clean-room open-source implementation.
Not affiliated with Google or any proprietary NanoBanana project.


---

##  GitHub push commands

```bash
git init
git add .
git commit -m "Initial release: OpenNanoBanana nano LLM"
git branch -M main
git remote add origin https://github.com/<your-username>/opennanobanana.git
git push -u origin main
```

## Live Demo

### Backend
```bash
uvicorn app.main:app --reload
```

🍌 OpenNanoBanana — Hugging Face Release Guide
What you’ll end up with
* hf.co/<you>/opennanobanana
* hf.co/spaces/<you>/opennanobanana-demo
A model people can actually try

1️⃣ Prerequisites (one-time)
```bash
pip install huggingface_hub
huggingface-cli login
```
Create a token on HF → Write access
