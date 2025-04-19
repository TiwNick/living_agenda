import os

class Task:
    tasks = []

    def __init__(self, tittle, description, time):
        '''construtor para a task'''
        self._title = tittle.title()
        self._description = description.upper()
        self._time = []
        Task.tasks.append(self)

    def __str__(self):
        '''Funcao para exibir o nome e a descricao da tarefa'''
        return f'{self._title} | {self._description} | {self._time}'

    @classmethod
    def list_activities(cls):
        '''Funcao para listar as tarefas'''
        print(f'{'Task'.ljust(25)} | {'Description'.ljust(25)} | {'Time'.ljust(25)}')
        for task in cls.tasks:
            print(f'{tasks._title.ljust(25)} | {tasks._description.ljust(25)} | {str(tasks.time).ljust(25)}')
