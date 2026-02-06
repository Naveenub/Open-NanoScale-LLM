from transformers import AutoModelForCausalLM
from peft import PeftModel

base = AutoModelForCausalLM.from_pretrained("Qwen2.5-1.5B")
lora = PeftModel.from_pretrained(base, "onb-lora")

merged = lora.merge_and_unload()
merged.save_pretrained("merged-model")
