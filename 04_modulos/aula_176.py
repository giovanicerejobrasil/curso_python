"""
os + shutil - Copiando arquivos com Python

- Copiar -> shutil.copy

1 - Copiar arquivos de uma pasta para outra
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
ORIGINAL_DIR = os.path.join(DESKTOP, 'Development', 'EXEMPLE')
NEW_DIR = os.path.join(DESKTOP, 'Development', 'EXEMPLE_NEW')

print(HOME)
print(DESKTOP)
print(ORIGINAL_DIR)
print(NEW_DIR)

os.makedirs(NEW_DIR, exist_ok=True)

for root, dirs, files in os.walk(ORIGINAL_DIR):
    for dir_ in dirs:
        dir_path_new = os.path.join(
            root.replace(ORIGINAL_DIR, NEW_DIR), dir_
        )
        os.makedirs(dir_path_new, exist_ok=True)

    for file_ in files:
        file_path = os.path.join(root, file_)
        file_path_new = os.path.join(
            root.replace(ORIGINAL_DIR, NEW_DIR), file_
        )
        shutil.copy(file_path, file_path_new)

print('COPIADO COM SUCESSO...')
