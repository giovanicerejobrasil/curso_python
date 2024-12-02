"""
Usando subprocess para executar e comandos externos subprocess é um módulo do
Python para executar processos e comandos externos no seu programa.

O método mais simples para atingir o objetivo é usando subprocess.run().
Argumentos principais de subprocess.run():
- stdout, stdin e stderr -> Redirecionam saída, entrada e erros
- capture_output -> captura a saída e erro para uso posterior
- text -> Se True, entradas e saídas serão tratadas como texto e
automaticamente codificadas ou decodificadas com o conjunto de
caracteres padrão da plataforma (geralmente UTF-8).
- shell -> Se True, terá acesso ao shell do sistema. Ao usar shell (True),
recomendo enviar o comando e os argumentos juntos.
- executable -> pode ser usado para especificar o caminho do executável que
iniciará o subprocesso.

Retorno:
stdout, stderr, returncode e args

Importante: a codificação de caracteres do Windows pode ser
diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
mac, use utf_8.

Comando de exemplo:
Windows: ping 127.0.0.1
Linux/Mac: ping 127.0.0.1 -c 4
"""
import subprocess
import sys


def print_division(
    text='',
    sep_text='=',
    num_repeat=35,
    jump=False
):
    print() if jump else ...
    print(sep_text * num_repeat, sep='\n')
    print(text.upper(), end='\n\n')


system = sys.platform

cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'

# Windows
if system == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'  # cp1252, cp852, cp850

process_ = subprocess.run(
    cmd,
    capture_output=True,
    text=False,
    encoding=encoding,
    shell=False
)

print_division(text='sys.platform', jump=True)
print(sys.platform)

print_division(text='subprocess.run return', jump=True)
print(process_)

print_division(text='subprocess.run args', jump=True)
print(process_.args)

print_division(text='subprocess.run stdout', jump=True)
print(process_.stdout)

print_division(text='subprocess.run stderr', jump=True)
print(process_.stderr)

print_division(text='subprocess.run returncode', jump=True)
print(process_.returncode)

# Usando com shell=True
cmd = ['ls -lah /']
encoding = 'utf_8'

# Windows
if system == 'win32':
    cmd = ['dir /']
    encoding = 'cp850'  # cp1252, cp852, cp850

process_ = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encoding,
    shell=True
)

print_division(text='subprocess.run return (shell=true)', jump=True)
print(process_)

print_division(text='subprocess.run args (shell=true)', jump=True)
print(process_.args)

print_division(text='subprocess.run stdout (shell=true)', jump=True)
print(process_.stdout)

print_division(text='subprocess.run stderr (shell=true)', jump=True)
print(process_.stderr)

print_division(text='subprocess.run returncode (shell=true)', jump=True)
print(process_.returncode)
