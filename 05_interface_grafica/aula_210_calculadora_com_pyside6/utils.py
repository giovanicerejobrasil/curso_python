import re

NUM_DOT_PERCENT_REGEX = re.compile(r'^[0-9.]$')


# Verifica se a string é um número ou um ponto (.)
def isNumOrDot(string: str) -> bool:
    return bool(NUM_DOT_PERCENT_REGEX.search(string))


# Converte uma string para int ou float
def convertToNumber(string: str | int | float) -> int | float:
    number = float(string)

    if number.is_integer():
        number = int(number)

    return number


# Verifica se a string é um número válido
def isValidNumber(string: str) -> bool:
    isValid = False

    try:
        float(string)
        isValid = True
    except ValueError:
        isValid = False

    return isValid


# Verifica se a string é vazia
def isEmpty(string: str) -> bool:
    return len(string) == 0
