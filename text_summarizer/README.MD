# 📘 BART-LARGE-CNN Text Summarizer

Full-Document Summarizer with Short / Medium / Long Options  
Runs locally on Mac using Transformers + PyTorch (MPS acceleration)

---

## 🚀 Features

✔ Summarize _long_ documents (peste 1.000 cuvinte)  
✔ 3 modes: **Short**, **Medium**, **Long**  
✔ Auto-chunking pentru texte foarte mari  
✔ Folosește modelul profesionist: `facebook/bart-large-cnn`  
✔ 100% local, fără API

---

## 🧠 How it works

1. Userul lipește un text de orice lungime
2. Programul împarte textul în segmente
3. Face rezumate individuale
4. Le combină într-un „rezumat al rezumatelor”
5. Creează o versiune finală coerentă

---

## ▶️ Run the summarizer

Asigură-te că ești în environment-ul tău:

```bash
source nlp_env/bin/activate
```
