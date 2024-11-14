"""
json.dumps e json.loads com strings + typing.TypedDict

Ao converter de Python para JSON:
Python        JSON
dict          object
list, tuple   array
str           string
int, float    number
True          true
False         false
None          null
"""
import json
from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


string_json = """
{
  "title": "Esquadrão Classe A",
  "original_title": "The A-Team",
  "is_movie": true,
  "imdb_rating": 6.7,
  "year": 2010,
  "characters": ["Hannibal", "Face", "Murdock", "B.A. Baracus"],
  "budget": null
}
"""

movie: Movie = json.loads(string_json)

print_division(text='JSON LOADS WITH PPRINT')
pprint(movie, width=40)

print_division(text='JSON LOADS KEYS WITH TYPEDDICT', jump=True)
print(movie['title'])
print(movie['characters'][0])
print(movie['year'] + 10)

print_division(text='JSON DUMPS', jump=True)
json_string = json.dumps(movie, ensure_ascii=False, indent=2)
print(json_string)
