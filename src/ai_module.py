from transformers import pipeline

# Use distilgpt2 (small, free model)
generator = pipeline("text-generation", model="distilgpt2")

def generate_script(concept, content):
    prompt = f"Explain the concept '{concept}' in simple terms:\n{content}\nExplanation:"
    result = generator(prompt, max_new_tokens=256, truncation=True, do_sample=True)[0]["generated_text"]
    return result

def generate_slides(concept, content):
    return [
        f"📘 Title: {concept}",
        f"📖 Definition: {content.split('.')[0]}",
        "✅ Key Points:",
        "- Easy to understand",
        "- Practical examples",
        "- Real-world applications"
    ]
