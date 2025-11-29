from transformers import pipeline

print("\n" * 50)
print("Live Translator English ↔ Romanian")
print("Type 'exit' to quit\n")

# Engleză → Română
en_to_ro = pipeline("translation_en_to_ro", model="Helsinki-NLP/opus-mt-en-ro")

# Română → Engleză (model universal care merge excelent)
ro_to_en = pipeline("translation", model="facebook/m2m100_418M")

while True:
    text = input("You: ").strip()
    
    if text.lower() == "exit":
        print("Bye! 👋")
        break
    
    if not text:
        continue
    
    if any(c in "ăîâșțĂÎÂȘȚ" for c in text):
        # Română → Engleză
        translation = ro_to_en(text, src_lang="ro", tgt_lang="en")[0]['translation_text']
        print(f"→ EN: {translation}\n")
    else:
        # Engleză → Română
        translation = en_to_ro(text)[0]['translation_text']
        print(f"→ RO: {translation}\n")