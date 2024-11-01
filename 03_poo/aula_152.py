"""
Context Manager com classes - Criando e Usando gerenciadores de contexto

Você pode implementar seus próprios protocolos apenas implementando os dunder methods que o Python vai usar.

Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica onde o Python não está interessado no tipo, mas se alguns métodos existem no seu objeto para que ele funcione de forma adequada.

Duck Typing:
Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna como um pato, eu chamo aquele pássaro de pato.

Para criar um context manager, os métodos __enter__ e __exit__ devem ser implementados.

O método __exit__ receberá a classe de exceção, a exceção e o traceback. Se ele retornar True, exceção no with será suprimidas.

Ex.:
with open('aula149.txt', 'w') as arquivo:
    ...
"""


class MyOpenFile:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None

    def __enter__(self):
        print('ABRINDO ARQUIVO...')
        self._file = open(self.file_path, self.mode, encoding='utf8')

        return self._file

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO...')
        self._file.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        # exception_.add_note('Minha nota')

        # raise ConnectionError('Não foi possível conectar')

        # return True  # Exceção tratada


with MyOpenFile('poo/aula_152.txt', 'w') as file:
    file.write('LINHA 1\n')
    file.write('LINHA 2\n', 321)
    file.write('LINHA 3\n')

    print('WITH', file)
