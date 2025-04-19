import os

def show_menu():
    print('1. Create new task')
    print('2. List tasks')
    print('3. Leave\n')

def show_subtitle(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def leave_program():
    show_subtitle('...finishing...')


def create_task():
    task_name = input("What's your task's title?: ")
    task_desc = input("Describe your task: ")
    task_time = input("How long time you'll take to complete your task?: ")
    task_data = {'title': task_name, 'description': task_desc, 'time to complete': task_time}
    tasks.append(task_data)
    print(f'The task {task_name} was succesfully registred!')
    back_menu()

def back_menu():
    input('\nPress any key for back to the menu...')
    main()

def invalid_option():
    print('Please insert a valid option!\n')
    back_menu()

def list_tasks():
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for task in tasks:
        task_name = task['title']
        task_description = task['description']
        task_time = task['time']
        print(f'- {task_name.ljust(20)} | {task_description.ljust(20)} | {task_time}')

    back_menu()

def choose_one():
    try:
        choosen = int(input('Choose one option: '))
        # choosen = int(choosen)

        if choosen == 1: 
            create_task()
        elif choosen == 2: 
            list_tasks()
        elif choosen == 3: 
            leave_program()
        else: 
            invalid_option()
    except:
        invalid_option()


def main():
    os.system('cls')
    #exibir_nome_programa()
    show_menu()
    #escolher_opcao()

if __name__ == '__main__':
    main()