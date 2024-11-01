"""
Relações entre classes: associação, agregação e composição

Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.

Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).

Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
"""


class Writer:
    def __init__(self, name) -> None:
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WritingTool:
    def __init__(self, name) -> None:
        self.name = name

    def toWrite(self):
        return f'{self.name} está escrevendo'


writer = Writer('Giovani')
pen = WritingTool('Caneta Bic')
typewriter = WritingTool('Máquina de Escrever')

writer.tool = typewriter

print(pen.toWrite())
print(typewriter.toWrite())
print(writer.tool.toWrite())
