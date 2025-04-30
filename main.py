import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models.task import Task
from models.subtask import Subtask

app = FastAPI(
    title="Living Agenda API",
    description="API para gerenciamento de tarefas",
    version="1.0.0",
    contact={
        "name": "Nick",
        "url": "https://github.com/TiwNick",
        "email": "nicollaslucena1505@gmail.com",
    },
)

# ===== Banco de dados em memória (temporário) =====
#tasks: List[Task] = [
 #   Task(title="TESTE", description="TESTE", time_to_complete="1 MINUTES"),
  #  Task(title="TESTE TWO", description="TESTE TWO", time_to_complete="2 MINUTES"),
   # Task(title="TESTE THREE", description="TESTE THREE", time_to_complete="3 MINUTES")
#]

# ===== Rotas =====
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Hello from Render"}

@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task, tags=["Tasks"])
def create_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, updated_task: Task):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = updated_task
    return updated_task

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted = tasks.pop(task_id)
    return {"message": f"Task '{deleted.title}' deleted successfully"}

tasks = [{'title':'TESTE','description':'TESTE','time to complete':'1 MINUTES'},
         {'title':'TESTE TWO','description':'TESTE TWO','time to complete':'2 MINUTES'},
         {'title':'TESTE THREE','description':'TESTE THREE','time to complete':'3 MINUTES'}]

subtasks = [{'title':'test','description':'test','time to complete':'1 minute'},
         {'title':'test two','description':'test two','time to complete':'2 minutes'},
         {'title':'test three','description':'test three','time to complete':'3 minutes'}]

def show_menu():
    print('1. create new task')
    print('2. list tasks')
    print('3. edit task')
    print('4. leave\n')

def back_menu():
    input('\nPress any key for back to the menu...')
    main()

def invalid_option():
    print('Please insert a valid option!\n')
    back_menu()    

def show_subtitle(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def leave_program():
    show_subtitle('...finishing...')


def create_task():
    task_name = input("what's ur task's title?: ")
    task_desc = input("describe ur task: ")
    task_time = input("how long time you'll take to complete ur task?: ")
    task_data = {'title': task_name, 'description': task_desc, 'time to complete': task_time}
    tasks.append(task_data)
    print(f'the task {task_name} was succesfully registred!')
    back_menu()

def list_tasks():
    print(f"{'title'.ljust(22)} | {'description'.ljust(20)} | time to complete")
    for task in tasks:
        task_name = task['title']
        task_description = task['description']
        task_time = task['time to complete']
        print(f'- {task_name.ljust(20)} | {task_description.ljust(20)} | {task_time}')

    back_menu()

def editing_act():
    if not tasks or not subtasks:
        print("No activity available to edit.")
        back_menu()
        return

    print("\nWhich task do you want to edit?\n")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task['title']}")

    chosen = input("\nEnter the task number: ")

    if not chosen.isdigit():
        print("Invalid input. Please enter a number.")
        back_menu()
        return

    index = int(chosen) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        back_menu()
        return

    task = tasks[index]

    print("\nLeave blank if you don't want to change the field.")
    new_title = input(f"New title [{task['title']}]: ") or task['title']
    new_desc = input(f"New description [{task['description']}]: ") or task['description']
    new_time = input(f"New time to complete [{task['time']}]: ") or task['time']

    task['title'] = new_title
    task['description'] = new_desc
    task['time'] = new_time

    print("\n✅ Task updated successfully!")
    back_menu()


def choose_one():
    try:
        choosen = int(input('choose one option: '))
        # choosen = int(choosen)

        if choosen == 1: 
            create_task()
        elif choosen == 2: 
            list_tasks()
        elif choosen == 3: 
            editing_act()
        elif choosen == 4: 
            leave_program()
        else: 
            invalid_option()
    except:
        invalid_option()


def main():
    os.system('clear')
    #exibir_nome_programa()
    show_menu()
    #escolher_opcao()
    choose_one()

if __name__ == '__main__':
    main()
