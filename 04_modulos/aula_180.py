"""
json.dump e json.load com arquivos
"""
import json
import os
from pprint import pprint


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


FILE_NAME = 'aula_180.json'
FILE_ABSOLUT_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

movie = {
    "title": "Esquadrão Classe A",
    "original_title": "The A-Team",
    "is_movie": True,
    "imdb_rating": 6.7,
    "year": 2010,
    "characters": ["Hannibal", "Face", "Murdock", "B.A. Baracus"],
    "budget": None
}
with open(FILE_ABSOLUT_PATH, 'w') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with open(FILE_ABSOLUT_PATH, 'r') as file:
    json_movie = json.load(file)

print_division(text='ORIGINAL MOVIE')
pprint(movie)

print_division(text='JSON MOVIE CONVERTED', jump=True)
pprint(json_movie)
