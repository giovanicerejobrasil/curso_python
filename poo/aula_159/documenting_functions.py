"""
Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma já é bastante conhecida.
"""

variable_1 = 1


def sum_(x: int | float, y: int | float) -> int | float:
    """Soma x e y

    Este módulo contém funções e exemplos de documentação de funções.
    A função soma já é bastante conhecida.

    Args:
        x (int | float): Número 1
        y (int | float): Número 2

    Returns:
        int | float: Retorna a soma entre x e y
    """


def multiply(
    x: int | float,
    y: int | float,
    z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y e, se "z" for enviado é multiplicado z, y e z.

    Args:
        x (int | float): Número 1
        y (int | float): Número 2
        z (int | float | None, optional): Número. Defaults to None.

    Returns:
        int | float: Retorna a multiplicação entre x e y e/ou z
    """
    if z is None:
        return x * y
    return x * y * z


variable_2 = 2
variable_3 = 3
variable_4 = 4
