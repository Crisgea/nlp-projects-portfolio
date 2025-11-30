import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Încărcăm Mistral 7B local (prima dată durează 2-3 minute)
print("Încărcare Mistral 7B... așteaptă...")
chatbot = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3", device_map="auto")

def send():
    prompt = entry.get("1.0", tk.END).strip()
    if not prompt or prompt.lower() == "exit":
        root.destroy()
        return
    
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, "You: " + prompt + "\n", "user")
    chat.insert(tk.END, "Mistral: thinking...\n", "thinking")
    chat.config(state=tk.DISABLED)
    
    response = chatbot(f"<s>[INST] {prompt} [/INST]", max_new_tokens=500)[0]['generated_text']
    answer = response.split("[/INST]")[-1].strip()
    
    chat.config(state=tk.NORMAL)
    chat.delete("end-2l", "end-1l")
    chat.insert(tk.END, "Mistral: " + answer + "\n\n", "bot")
    chat.config(state=tk.DISABLED)
    chat.see(tk.END)
    entry.delete("1.0", tk.END)

# Fereastra
root = tk.Tk()
root.title("Mistral 7B Local Chatbot – Cristina Geafar")
root.geometry("1000x700")
root.configure(bg="#1e1e1e")

chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#2d2d2d", fg="white", font=("Arial", 12))
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat.tag_config("user", foreground="#4fc3f7", font=("Arial", 12, "bold"))
chat.tag_config("bot", foreground="#b2ff59")
chat.tag_config("thinking", foreground="#ff9800")

entry = tk.Text(root, height=4, bg="#3a3a3a", fg="white", font=("Arial", 12))
entry.pack(padx=10, pady=(0,10), fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send, bg="#4fc3f7", fg="white", font=("Arial", 12, "bold"))
send_btn.pack(pady=5)

chat.config(state=tk.NORMAL)
chat.insert(tk.END, "Mistral 7B Local Chatbot is ready!\nType 'exit' to quit\n\n", "bot")
chat.config(state=tk.DISABLED)

root.mainloop()