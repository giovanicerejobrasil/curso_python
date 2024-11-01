frase = """O Python é uma linguagem de programação multiparadigma.
O Python foi criado por Guido van Rossum"""

frase = """Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe clara e concisa, o que a torna ideal tanto para iniciantes quanto para programadores experientes. Sua legibilidade e facilidade de aprendizado a tornaram uma das linguagens mais populares do mundo. Python é utilizada em diversas áreas, como desenvolvimento web, ciência de dados, inteligência artificial e automação de tarefas. A vasta comunidade de desenvolvedores Python e a grande quantidade de bibliotecas disponíveis contribuem para sua versatilidade e poder.
Uma das principais vantagens do Python é sua interpretação, o que significa que o código pode ser executado linha por linha, facilitando a depuração e o desenvolvimento iterativo. Além disso, Python é uma linguagem multiparadigma, suportando tanto a programação procedural quanto a orientada a objetos. Essa flexibilidade permite que os programadores escolham o estilo de programação que melhor se adapta ao problema a ser resolvido. Com Python, a programação se torna mais intuitiva e produtiva, permitindo que os desenvolvedores se concentrem na lógica do problema em vez de se preocupar com detalhes técnicos da linguagem."""

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):
  letra_atual = frase[i]

  qtd_apareceu = frase.count(letra_atual)

  if letra_atual == ' ':
    i+=1
    continue

  if qtd_apareceu > qtd_mais_vezes:
    qtd_mais_vezes = qtd_apareceu
    letra_mais_vezes = letra_atual

  i+=1

print(f"""A letra que mais apareceu foi "{letra_mais_vezes}" com {qtd_mais_vezes} vez(es).""")