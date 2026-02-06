from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

model = AutoModelForCausalLM.from_pretrained("Qwen2.5-1.5B")
tokenizer = AutoTokenizer.from_pretrained("Qwen2.5-1.5B")

lora = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora)

trainer = SFTTrainer(
    model=model,
    train_dataset="data/processed/train.jsonl",
    tokenizer=tokenizer,
    max_seq_length=2048
)

trainer.train()
model.save_pretrained("onb-lora")
