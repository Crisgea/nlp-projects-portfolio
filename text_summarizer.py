from transformers import pipeline

# Modelul pentru rezumate (cel mai bun și descărcat)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

print("Text Summarizer – rezumate instant")
print("Scrie 'exit' ca să ieși\n")

while True:
    text = input("Paste text (long article): ").strip()
    
    if text.lower() == "exit":
        print("Bye! 👋")
        break
    
    if len(text) < 50:
        print("Text prea scurt – încearcă un articol lung\n")
        continue
    
    print("Generez rezumatul...\n")
    
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    print("Rezumat:")
    print(summary)
    print("\n" + "-" * 60 + "\n")