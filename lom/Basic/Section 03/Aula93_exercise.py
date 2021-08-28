# import os


def menu():
    # print("\n" * os.get_terminal_size().lines)
    print(f'\n{" Lista de tarefas ":=^25}\n')
    print('1 - Adicionar tarefas')
    print('2 - listar tarefas')
    print('3 - desfazer tarefa')
    print('4 - refazer tarefa')
    print('5 - Sair do programa')
    print('\n' + '-' * 50)
    return input('Digite uma opção: ')


def adicionar_tarefa(tarefa, lista):
    if tarefa not in lista:
        lista.append(tarefa)


def listar_tarefas(lista):
    print(f'\n{" Lista de tarefas ":=^25}\n')
    for tarefa in lista:
        print(tarefa)


def desfazer_tarefa(todo, redo):
    if not todo:
        print('Nada para desfazer')
    else:
        ultima_tarefa = todo.pop()
        redo.append(ultima_tarefa)
        print('Tarefa excluída')


def refazer_tarefa(todo, redo):
    if not redo:
        print('Nada para refazer')
    else:
        ultima_tarefa = redo.pop()
        todo.append(ultima_tarefa)
        print('Tarefa recuperada')


if __name__ == '__main__':
    todo_list = []
    redo_list = []
    while True:
        option = menu()
        if option == '1':
            tarefa = input('Descreva a tarefa em poucas palavras: ')
            adicionar_tarefa(tarefa, todo_list)
        elif option == '2':
            listar_tarefas(todo_list)
        elif option == '3':
            desfazer_tarefa(todo_list, redo_list)
        elif option == '4':
            refazer_tarefa(todo_list, redo_list)
        elif option == '5':
            print('Fim do programa')
            break
