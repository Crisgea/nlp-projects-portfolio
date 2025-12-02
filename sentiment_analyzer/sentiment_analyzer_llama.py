import subprocess
import json
import sys
from datetime import datetime

EMOJI = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😡",
    "fear": "😨",
    "surprise": "😲",
    "disgust": "🤢",
    "neutral": "😐"
}

def query_llama(prompt: str) -> str:
    process = subprocess.Popen(
        ["ollama", "run", "llama3.1"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, error = process.communicate(prompt)
    return output.strip()

def normalize_result(data):
    if "main_emotion" not in data:
        data["main_emotion"] = "neutral"

    if "confidence" not in data:
        data["confidence"] = 1.0

    if "top_3" not in data:
        data["top_3"] = [{"emotion": "neutral", "score": 1.0}]

    new_top3 = []
    for item in data["top_3"]:
        if isinstance(item, str):
            new_top3.append({"emotion": item, "score": 0.0})
        elif isinstance(item, dict):
            emo = item.get("emotion", "neutral")
            score = item.get("score", 0.0)
            new_top3.append({"emotion": emo, "score": score})
        else:
            new_top3.append({"emotion": "neutral", "score": 0.0})

    data["top_3"] = new_top3
    return data

def classify_emotion(text: str):
    prompt = f"""
You are an expert emotion classification model.
You MUST choose the emotion that best matches the text.
Avoid using "neutral" unless the text is completely emotionless and factual.

EMOTION DEFINITIONS:
- joy: positive feelings, excitement, happiness, warmth, enthusiasm
- sadness: sorrow, loss, disappointment
- anger: frustration, irritation, hostility
- fear: anxiety, worry, dread
- surprise: shock, unexpected reactions
- disgust: rejection, aversion
- neutral: no emotion at all

TASK:
Analyze the emotional tone of the text.
Return ONLY valid JSON structured like this:

{{
 "main_emotion": "joy|sadness|anger|fear|surprise|disgust|neutral",
 "confidence": 0.0,
 "top_3": [
   {{"emotion": "joy", "score": 0.0}},
   {{"emotion": "surprise", "score": 0.0}},
   {{"emotion": "neutral", "score": 0.0}}
 ]
}}

Choose the emotion with highest intensity.
If the text expresses strong happiness → choose joy.
If it contains excitement or amazement → add surprise.
Only choose neutral if the text has ZERO emotional wording.

TEXT TO ANALYZE:
\"\"\"{text}\"\"\"
"""

    response = query_llama(prompt)

    try:
        json_start = response.index("{")
        data = json.loads(response[json_start:])
        data = normalize_result(data)
        return data
    except:
        return {
            "main_emotion": "neutral",
            "confidence": 1.0,
            "top_3": [{"emotion": "neutral", "score": 1.0}]
        }

def save_to_history(text, result):
    with open("emotion_history.txt", "a", encoding="utf-8") as f:
        f.write("\n---\n")
        f.write(f"{datetime.now()}\n")
        f.write(f"TEXT:\n{text}\n")
        f.write(json.dumps(result, indent=4))
        f.write("\n")

def format_output(result):
    main = result["main_emotion"]
    emoji = EMOJI.get(main, "")
    conf = result["confidence"]

    out = f"\nmain_emotion: {main} {emoji} ({conf:.2f})\n"

    out += "\nTop 3:\n"
    for item in result["top_3"]:
        e = item["emotion"]
        s = item["score"]
        out += f"- {e} {EMOJI.get(e,'')} ({s:.2f})\n"

    return out

def start_chat():
    print("=== LLaMA 3.1 Emotion Analyzer — Enhanced Mode ===")
    print("Commands:")
    print("start   → begin entering text")
    print("analyze → process stored text")
    print("exit    → quit\n")

    stored_text = ""

    while True:
        cmd = input("Command: ").strip().lower()

        if cmd == "exit":
            print("Goodbye.")
            break

        if cmd == "start":
            print("\nPaste your text. Finish with an EMPTY LINE:")
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
            stored_text = "\n".join(lines)
            print("\nText stored. Type 'analyze' to process.\n")
            continue

        if cmd == "analyze":
            if stored_text.strip() == "":
                print("No text stored. Use 'start' first.\n")
                continue

            result = classify_emotion(stored_text)
            save_to_history(stored_text, result)
            print(format_output(result))
            print("\nReady for next command.\n")
            continue

        print("Unknown command.\n")

if __name__ == "__main__":
    start_chat()