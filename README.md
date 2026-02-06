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

Inference
python scripts/inference.py

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
