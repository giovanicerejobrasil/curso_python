"""
random tem geradores de números pseudoaleatórios

Obs.: números pseudoaleatórios significa que os números
parecem ser aleatórios, mas na verdade não são. Portanto,
este módulo não deve ser usado para segurança ou uso criptográfico.

O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
a saída pode ser previsível.
doc: https://docs.python.org/pt-br/3/library/random.html
"""
import random
import time


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


"""
Funções:
seed
  -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
"""
print_division(text='RANDOM SEED')
random.seed(time.time())
print(time.time())

seed_ = 0
# random.seed(seed_)
# print(seed_)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)

print_division(text='RANDOM R_RANGE', jump=True)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)

print_division(text='RANDOM R_INT', jump=True)
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)

print_division(text='RANDOM R_UNIFORM', jump=True)
print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
names = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(names)

print_division(text='RANDOM SHUFFLE', jump=True)
print(names)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
new_names = random.sample(names, k=3)

print_division(text='RANDOM SAMPLE', jump=True)
print(names)
print(new_names)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
new_names = random.choices(names, k=3)

print_division(text='RANDOM CHOICES', jump=True)
print(names)
print(new_names)

# random.choice(Iterável) -> Escolhe um elemento do iterável

print_division(text='RANDOM CHOICE', jump=True)
print(random.choice(names))
