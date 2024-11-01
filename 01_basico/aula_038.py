"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop Infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 100:
  contador += 1

  if contador == 50:
    break

  if contador % 2 == 0:
    continue

  print(contador)
