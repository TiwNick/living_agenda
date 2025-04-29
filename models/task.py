import os
from abc import ABC, abstractmethod

class Task(ABC):
    tasks = []

    def __init__(self, tittle, description, time):
        '''construtor para a task'''
        self._title = tittle.title()
        self._description = description.upper()
        self._time = []
        Task.tasks.append(self)

    def __str__(self):
        '''Funcao para exibir o nome e a descricao da task'''
        return f'{self._title} | {self._description} | {self._time}'

    @classmethod
    def list_tasks(clear):
        '''Funcao para listar as tarefas'''
        print(f'{'title'.ljust(25)} | {'description'.ljust(25)} | {'time to complete'.ljust(25)}')
        for task in clear.tasks:
            print(f'{task._title.ljust(25)} | {task._description.ljust(25)} | {str(task.time).ljust(25)}')