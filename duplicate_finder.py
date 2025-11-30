import os
import hashlib
from collections import defaultdict

print("Duplicate Cleaner – Mac M3 Ultra (versiune FINALĂ)")
print("Ignoră fișierele ascunse și șterge doar duplicatele reale\n")

while True:
    folder = input("Cale folder (ex: Downloads sau /Volumes/NumeDisc): ").strip()
    
    if folder.lower() == "exit":
        print("Bye! 👋")
        break
    
    if folder == "Downloads":
        folder = "/Users/cristinageafar/Downloads"
    
    if not os.path.exists(folder):
        print("Folderul nu există – încearcă iar\n")
        continue
    
    print(f"Scanez {folder} ...")
    
    duplicates = defaultdict(list)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Ignorăm fișierele ascunse de Mac (încep cu ._)
            if file.startswith("._"):
                continue
                
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.heic', '.mov', '.mp4')):
                path = os.path.join(root, file)
                try:
                    file_hash = hashlib.md5(open(path, 'rb').read()).hexdigest()
                    duplicates[file_hash].append(path)
                except:
                    continue
    
    dup_list = [paths for paths in duplicates.values() if len(paths) > 1]
    
    if not dup_list:
        print("Nu am găsit duplicate – folder curat! 🎉\n")
    else:
        total = sum(len(paths)-1 for paths in dup_list)
        print(f"Am găsit {total} duplicate reale – le șterg acum...\n")
        
        deleted = 0
        for paths in dup_list:
            keep = paths[0]
            for dup in paths[1:]:
                try:
                    os.remove(dup)
                    print(f"ȘTERS: {os.path.basename(dup)}")
                    deleted += 1
                except:
                    pass  # ignorăm orice eroare (fișiere blocate etc.)
        
        print(f"\nGATA! Am șters {deleted} fișiere duplicate reale!")
        print("Spațiu eliberat cu succes! 🚀\n")
    
    print("-" * 60)