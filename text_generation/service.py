import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
model_path = "./gpt2-shakesepeare"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)


model.eval()


def generate_text(prompt: str, temperature: float = 0.7, max_length: int = 100) -> str:
    # Generate text
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        temperature=temperature,
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text
