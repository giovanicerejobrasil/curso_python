"""
Exercício - Lista de tarefas com desfazer e refazer
Música para codar =)
Everybody wants to rule the world - Tears for fears
todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café',] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
"""
import os
import json


def show_list(todo_list):
    print('LISTA DE TAREFAS')

    if not todo_list:
        todo_list = open_file(todo_list, FILE_PATH)

    if not todo_list:
        print('NENHUM ITEM ADICIONADO À LISTA')
        print()
        return

    for task in todo_list:
        print(f'  - {task}')
    print()
    return


def undo(todo_list, excluded_items_list):
    if not todo_list:
        print('Ação não realizada')
        print()
        return

    tarefa = todo_list.pop()
    excluded_items_list.append(tarefa)

    print(f'Tarefa [{tarefa.upper()}] removida da lista')
    print()


def redo(todo_list, excluded_items_list):
    if not excluded_items_list:
        print('Ação não realizada')
        print()
        return

    tarefa = excluded_items_list.pop()
    todo_list.append(tarefa)

    print(f'Tarefa [{tarefa.upper()}] readicionada a lista')
    print()


def add_task(task, todo_list):
    if not task:
        print('Nenhuma tarefa ou comando foi digitado')
        print()
        return

    todo_list.append(task)

    print(f'TAREFA [{task.upper()}] Adicionada')
    print()


def clear():
    os.system('clear')


def open_file(todo_list, file_path):
    data = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print('ARQUIVO NÃO EXISTE')
        save_file(todo_list, file_path)

    return data


def save_file(todo_list, file_path):
    data = todo_list

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )

    return data


FILE_PATH = 'intermediario/aula_121.json'
commands = ['listar', 'desfazer', 'refazer', 'clear', 'exit']
todo_list = open_file([], FILE_PATH)
excluded_items_list = []


while True:
    print(f'Comandos: {commands}')
    user_choice = input('Digite uma tarefa ou um comando: ').lower().strip()

    if (user_choice in commands):
        print(f'COMANDO [{user_choice.upper()}]')

        if user_choice == commands[0]:
            show_list(todo_list)

        if user_choice == commands[1]:
            undo(todo_list, excluded_items_list)
            show_list(todo_list)

        if user_choice == commands[2]:
            redo(todo_list, excluded_items_list)
            show_list(todo_list)

        if user_choice == commands[3]:
            clear()

        if user_choice == commands[4]:
            exit()

    else:
        add_task(user_choice, todo_list)

    save_file(todo_list, FILE_PATH)
