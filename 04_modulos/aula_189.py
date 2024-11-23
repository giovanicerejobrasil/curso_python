"""
ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
"""
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
PATH_ROOT = Path(__file__).parent
PATH_ZIP_DIR = PATH_ROOT / 'aula_189_dir_zip'
PATH_COMPACT = PATH_ROOT / 'aula_189_compact.zip'
PATH_DESCOMPACT = PATH_ROOT / 'aula_189_descompact'

shutil.rmtree(PATH_ZIP_DIR, ignore_errors=True)
Path.unlink(PATH_COMPACT, missing_ok=True)
shutil.rmtree(str(PATH_COMPACT).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(PATH_DESCOMPACT, ignore_errors=True)

# rise Exception()

# Cria o diretório para a aula
PATH_ZIP_DIR.mkdir(exist_ok=True)


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text.upper(), end='\n\n')


def create_files(qtd: int, zip_dir: Path):
    for i in range(qtd):
        text = f'file_{i}'

        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)


create_files(10, PATH_ZIP_DIR)

# Criado um .zip e adicionando arquivos
print_division(text='CREATE ZIP FILE')
with ZipFile(PATH_COMPACT, 'w') as zip:
    for root, dirs, files in os.walk(PATH_ZIP_DIR):
        for file in files:
            print(file)
            zip.write(os.path.join(root, file), file)

# Lendo os arquivos de um .zip
print_division(text='READ ZIP FILE', jump=True)
with ZipFile(PATH_COMPACT, 'r') as zip:
    for file in zip.namelist():
        print(file)

# Descompactando os arquivos de um .zip
print_division(text='DESCOMPACT ZIP FILE', jump=True)
with ZipFile(PATH_COMPACT, 'r') as zip:
    zip.extractall(PATH_DESCOMPACT)

print('DESCOMPACTADO COM SUCESSO')
