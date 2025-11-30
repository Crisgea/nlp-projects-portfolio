from transformers import pipeline

print("Traducător în orice limbă")
print("Scrie: text + ' in ' + limba (ex: Hello in Romanian)\n")

translator = pipeline("translation", model="facebook/m2m100_418M")

while True:
    text = input("Tu: ").strip()
    
    if text.lower() == "exit":
        print("Bye!")
        break
    
    if " in " not in text.lower():
        print("Scrie corect: text + ' in ' + limba\n")
        continue
    
    parts = text.lower().split(" in ")
    message = parts[0].strip()
    lang = parts[1].strip()
    
    languages = {
        "romanian": "ro", "english": "en", "french": "fr",
        "german": "de", "spanish": "es", "italian": "it"
    }
    
    if lang not in languages:
        print("Nu știu limba asta – încearcă: romanian, english, french...\n")
        continue
    
    result = translator(message, src_lang="en", tgt_lang=languages[lang])[0]['translation_text']
    print(f"→ {result}\n")