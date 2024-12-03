# type: ignore
"""
pypdf para manipular arquivos PDF

pypdf é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
extrair texto e imagens, manipular metadados, e mais.

A documentação contém todas as informações necessárias para usar pypdf.
Link: https://pypdf.readthedocs.io/en/stable/

- Ative seu ambiente virtual
- pip install pypdf
"""
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text.upper(), end='\n\n')


ROOT_DIR = Path(__file__). parent
ORIGINAL_DIR = ROOT_DIR / 'aula_200' / 'pdfs_originais'
NEW_DIR = ROOT_DIR / 'aula_200' / 'pasta_novos'
BACEN_REPORT = ORIGINAL_DIR / 'R20241129.pdf'

NEW_DIR.mkdir(exist_ok=True)

reader = PdfReader(BACEN_REPORT)

print_division(text='pdfreader pages len')
print(len(reader.pages))

print_division(text='pdfreader pages', jump=True)
for page in reader.pages:
    print(page)
    print()

print_division(text='pdfreader pages extract_text', jump=True)
page_0 = reader.pages[0]
print(page_0.extract_text())

print_division(text='pdfreader pages images', jump=True)
images = page_0.images
image_0 = images[0]

print(images)
print()
print(image_0)

with open(NEW_DIR / image_0.name, 'wb') as image:
    image.write(image_0.data)

print_division(text='pdfwriter with add_page', jump=True)
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_DIR / f'page_{i}.pdf', 'wb') as file:
        writer.add_page(page)
        writer.write(file)

print('PDF criado com sucesso...')

print_division(
    text='pdfwriter with append (pdfmerger is deprecated)', jump=True)
merger = PdfWriter()

files = [
    NEW_DIR / 'page_1.pdf',
    NEW_DIR / 'page_0.pdf',
]

for file in files:
    merger.append(file)

with open(NEW_DIR / 'merged.pdf', 'wb') as file:
    merger.write(file)

print('PDFs unidos com sucesso...')
