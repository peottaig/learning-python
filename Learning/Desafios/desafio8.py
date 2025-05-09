import os
import json

CAMINHO_DO_ARQUIVO = r"C:\\Users\\luigg\\learning-python\\Learning\\\\Dados\\listaExercicio8.json"


def listar(tarefas):  # Essa função realiza apenas os prints da lista de tarefas
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return

    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def salva_tarefas(tarefas, caminho_arquivo):
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(tarefas, arquivo)


def load_list(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        return json.load(arquivo)


tarefas = load_list(CAMINHO_DO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    if tarefa == 'listar':
        listar(tarefas)
        continue

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        salva_tarefas(tarefas, CAMINHO_DO_ARQUIVO)
        continue

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'clear':
        os.system('clear')
        continue

    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        salva_tarefas(tarefas, CAMINHO_DO_ARQUIVO)
        continue
