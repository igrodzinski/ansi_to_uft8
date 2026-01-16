import os

def convert_ansi_to_utf8(folder_path):
    # Rozszerzenia do sprawdzenia
    target_extension = ".sql"
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(target_extension):
            file_path = os.path.join(folder_path, filename)
            
            try:
                # Odczyt w formacie ANSI (windows-1250 dla PL)
                with open(file_path, 'r', encoding='windows-1250') as f:
                    content = f.read()
                
                # Zapis w formacie UTF-8
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Przekonwertowano: {filename}")
            except Exception as e:
                print(f"Błąd w pliku {filename}: {e}")

# Podaj ścieżkę do folderu
folder = "sciezka/do/twojego/folderu"
convert_ansi_to_utf8(folder)
