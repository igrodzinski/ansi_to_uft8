import os

def fix_encoding_recursive(root_folder):
    for root, _, files in os.walk(root_folder):
        for filename in files:
            if filename.lower().endswith(".sql"):
                file_path = os.path.join(root, filename)
                
                # 1. Próba odczytu jako UTF-8
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        f.read()
                    print(f"Pominięto (już jest UTF-8): {filename}")
                    continue 
                except UnicodeDecodeError:
                    # 2. Jeśli błąd, konwertuj z ANSI (windows-1250)
                    try:
                        with open(file_path, 'r', encoding='windows-1250') as f:
                            content = f.read()
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"SKONWERTOWANO: {filename}")
                    except Exception as e:
                        print(f"BŁĄD w pliku {filename}: {e}")

# Podaj ścieżkę
folder_glowny = "sciezka/do/folderu"
fix_encoding_recursive(folder_glowny)
