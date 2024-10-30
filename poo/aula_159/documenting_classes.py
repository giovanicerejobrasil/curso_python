"""Este é um módulo de exemplo

Este módulo contém funções e exemplos de documentação de funções.
A função soma já é bastante conhecida.
"""

variable_1 = 1


class Foo:
    """Esta é a classe de exemplo Foo

    Esta classe contém funções e exemplos de documentação de funções.
    """
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

    def bar(self, error_msg) -> int:
        """Sobe um erro de não implementação

        Args:
            error_msg (_type_): mensagem de erro que será exibida na exceção.

        Raises:
            NotImplementedError: Levanta um erro caso algo não tenha sido 
            definido.

        Returns:
            int: Retorna 0 ou 1
        """
        raise NotImplementedError(error_msg)


variable_2 = 2
variable_3 = 3
variable_4 = 4
