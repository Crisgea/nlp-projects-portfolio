from transformers import pipeline

print("\n" * 50)
print("MISTRAL 7B LOCAL – ChatGPT privat pe Mac-ul tău")
print("Scrie 'exit' ca să ieși\n")

# Modelul oficial Mistral 7B (cel mai bun open-source)
chatbot = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.3",
    device_map="auto",
    torch_dtype="auto"
)

while True:
    prompt = input("You: ").strip()
    
    if prompt.lower() == "exit":
        print("Bye! See you later! 👋")
        break
    
    if not prompt:
        continue
    
    print("Mistral gândește...\n")
    
    response = chatbot(
        f"<s>[INST] {prompt} [/INST]",
        max_new_tokens=400,
        temperature=0.7,
        do_sample=True
    )[0]['generated_text']
    
    answer = response.split("[/INST]")[-1].strip()
    print(f"Mistral: {answer}\n")