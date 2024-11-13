"""
os + shutil - Apagando, copiando, movendo e renomeando pastas com Python

Vamos copiar arquivos de uma pasta para outra.

Copiar -> shutil.copy
Copiar Árvore recursivamente -> shutil.copytree
Apagar Árvore recursivamente -> shutil.rmtree
Apagar arquivos -> os.unlink
Renomear/Mover -> shutil.move ou os.rename
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

shutil.rmtree(NEW_DIR, ignore_errors=True)
shutil.copytree(ORIGINAL_DIR, NEW_DIR)

shutil.rmtree(NEW_DIR + '_MOVE', ignore_errors=True)
shutil.move(NEW_DIR, NEW_DIR + '_MOVE')
# shutil.rmtree(NEW_DIR + '_MOVE', ignore_errors=True)
