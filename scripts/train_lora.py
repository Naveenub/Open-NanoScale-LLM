import yaml
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

with open("configs/lora.yaml") as f:
    lora_cfg = yaml.safe_load(f)

with open("configs/training.yaml") as f:
    train_cfg = yaml.safe_load(f)

model_name = "Qwen2.5-1.5B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto"
)

lora = LoraConfig(
    r=lora_cfg["r"],
    lora_alpha=lora_cfg["lora_alpha"],
    lora_dropout=lora_cfg["lora_dropout"],
    target_modules=lora_cfg["target_modules"],
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora)

dataset = load_dataset("json", data_files="data/processed/train.jsonl")["train"]

args = TrainingArguments(
    output_dir=train_cfg["output_dir"],
    per_device_train_batch_size=train_cfg["batch_size"],
    gradient_accumulation_steps=train_cfg["gradient_accumulation_steps"],
    learning_rate=train_cfg["learning_rate"],
    num_train_epochs=train_cfg["epochs"],
    fp16=train_cfg["fp16"],
    logging_steps=train_cfg["logging_steps"],
    save_steps=train_cfg["save_steps"],
    report_to="none"
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    tokenizer=tokenizer,
    args=args,
    max_seq_length=2048
)

trainer.train()
trainer.save_model(train_cfg["output_dir"])
