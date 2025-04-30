import os
from models.task import Task

class Subtask(Task):
    subtasks = []

    def __init__(self, tittle, description, time):
        '''construtor para a task'''
        super().self.__init__(tittle)
        self._description = description.upper()
        self._time = []
        Subtask.subtasks.append(self)

    def __str__(self):
        '''Funcao para exibir o nome e a descricao da subtask'''
        return f'{self._description} | {self._time}'

    @classmethod
    def list_subtasks(clear):
        '''Funcao para listar as subtasks'''
        print(f"{'title'.ljust(25)} | {'description'.ljust(25)} | {'time to complete'.ljust(25)}")
        for subtask in clear.subtasks:
            print(f'{subtask._title.ljust(25)} | {subtask._description.ljust(25)} | {str(subtask.time).ljust(25)}')
