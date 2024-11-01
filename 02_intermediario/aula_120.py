"""
Problema dos parâmetros mutáveis em funções python
"""


def add_client(name, list=None):
    if list is None:
        list = []

    list.append(name)
    return list


client_1 = add_client('Giovani')
add_client('Luanna', client_1)
add_client('Alex', client_1)

client_2 = add_client('Malu')
add_client('Mel', client_2)

client_3 = add_client('Maya')
add_client('Dani', client_3)

print(client_1)
print(client_2)
print(client_3)
