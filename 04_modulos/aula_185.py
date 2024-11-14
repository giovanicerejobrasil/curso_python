"""
secrets gera números aleatórios seguros
"""
import secrets
import time
import string as s
from secrets import SystemRandom as Sr


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text, end='\n\n')


print('SECRETS SYSTEMRANDOM')
random = secrets.SystemRandom()

"""
Funções:
seed
  -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
"""
print_division(text='RANDOM SEED (DON\'T WORK)', jump=True)
random.seed(time.time())
print(time.time())

seed_ = 345
random.seed(seed_)
print(seed_)

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

# PASSWORD
#   -> Gera uma senha aleatória com o módulo string.ascii_letters, string
# digits e string.punctuation e o SystemRandom.choices
print_division(
    text='RANDOM PASSWORD (STRING MODULE | SYSTEMRANDOM CHOICES)', jump=True)
alphabetic = s.ascii_letters + s.digits + s.punctuation
new_random_password = Sr().choices(alphabetic, k=35)
print(''.join(new_random_password))

# secrets.randbelow(int)
#   -> Gera um número inteiro aleatório dentro do intervalo 0 e n
print_division(text='SECRETS RANDBELOW', jump=True)
print(secrets.randbelow(999))

# secrets.randbelow(k: int)
#   -> Gera um número inteiro aleatório com a randomização de k bits
print_division(text='SECRETS RANDBITS', jump=True)
print(secrets.randbits(64))

# secrets.choice(int)
#   -> Escolhe um elemento do iterável
print_division(text='SECRETS CHOICE', jump=True)
int_numbers = [11, 12, 13, 26, 57, 89, 133]
print(int_numbers)
print(secrets.choice(int_numbers))

# secrets.token_bytes(nBytes: int)
#   -> Gera uma string de bytes aleatórios contendo nBytes
print_division(text='SECRETS TOKEN_BYTES', jump=True)
print(secrets.token_bytes(64))

# secrets.token_hex(nBytes: int)
#   -> Gera uma string aleatória de decimais
print_division(text='SECRETS TOKEN_HEX', jump=True)
print(secrets.token_hex(64))

# secrets.token_urlsafe(nBytes: int)
#   -> Gera uma string aleatória codificada em Base64
print_division(text='SECRETS TOKEN_URLSAFE', jump=True)
print(secrets.token_urlsafe(64))
