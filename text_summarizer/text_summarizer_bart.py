from transformers import pipeline

print("=== BART-LARGE-CNN Full-Document Summarizer ===")
print("Paste your text. When finished, type END on a new line.\n")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def get_text():
    print("(start typing; finish with END):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def chunk_text(text, max_words=350):
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

def summarize_chunk(chunk, max_len, min_len):
    return summarizer(
        chunk,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )[0]["summary_text"]

def full_summary(text, mode):
    words = len(text.split())

    # Config în funcție de opțiune
    if mode == "short":
        max_l, min_l = 60, 30
    elif mode == "long":
        max_l, min_l = 200, 120
    else:  # medium
        max_l, min_l = 120, 70

    # Dacă textul e scurt
    if words <= 350:
        return summarize_chunk(text, max_l, min_l)

    # Dacă textul e lung
    chunks = chunk_text(text)
    partial = [summarize_chunk(c, max_l, min_l) for c in chunks]
    combined = " ".join(partial)

    return summarize_chunk(combined, max_l, min_l)

while True:
    text = get_text()

    if text.lower().strip() == "exit":
        break

    if len(text.split()) < 20:
        print("Text too short.\n")
        continue

    print("\nChoose summary type:")
    print("1. Short (SEO/news)")
    print("2. Medium (recommended)")
    print("3. Long (detailed)")

    choice = input("Option (1/2/3): ").strip()

    if choice == "1":
        mode = "short"
    elif choice == "3":
        mode = "long"
    else:
        mode = "medium"

    print("\nGenerating summary...\n")
    result = full_summary(text, mode)

    print("=== SUMMARY ===\n")
    print(result)
    print("\n------------------------------------------------------------\n")