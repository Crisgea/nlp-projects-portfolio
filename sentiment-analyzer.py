from transformers import pipeline

# Cel mai bun model pentru sentiment în engleză
analyzer = pipeline("sentiment-analysis")

print("Sentiment Analyzer – scrie în engleză")
print("Scrie 'exit' ca să ieși\n")

while True:
    text = input("You: ")
    
    if text.lower() == "exit":
        break
    
    result = analyzer(text)[0]
    print(f"→ {result['label']} (confidence: {result['score']:.2f})\n")