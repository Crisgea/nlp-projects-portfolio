from transformers import pipeline

print("\n" * 50)
print("Question Answering Bot – English")
print("Paste ONE article, then ask as many questions as you want")
print("Type 'exit' to quit\n")

# Modelul cel mai bun și stabil pentru QA
qa = pipeline("question-answering", model="distilbert/distilbert-base-uncased-distilled-squad")

# 1. Citește articolul (o singură dată)
print("Paste your article (press Enter twice when finished):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

context = " ".join(lines).strip()

if not context:
    print("No article – bye!")
else:
    print(f"\nArticle loaded! ({len(context.split())} words)")
    print("You can now ask as many questions as you want:\n")
    
    # 2. Întrebări la nesfârșit pe același articol
    while True:
        question = input("Your question: ").strip()
        
        if question.lower() == "exit":
            print("Bye! See you later! 👋")
            break
            
        if not question:
            continue
            
        result = qa(question=question, context=context)
        print(f"Answer → {result['answer']}")
        print(f"Confidence: {result['score']:.3f}\n")