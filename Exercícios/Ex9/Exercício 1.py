def show_ls(todo_list):
    print()
    print('Tarefas:')
    print(todo_list)
    print()


def undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer.')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer.')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def add_ls(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma Tarefa ou [undo, redo, ls, leave]: ')

        if todo == 'leave':
            break
        elif todo == 'ls':
            show_ls(todo_list)
            continue
        elif todo == 'undo':
            undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            redo(todo_list, redo_list)
            continue

        add_ls(todo, todo_list)
