import os

class Activity:
    activities = []

    def __init__(self, tittle, description, time):
        '''construtor para a atividade'''
        self._title = tittle.title()
        self._description = description.upper()
        self._time = []
        Activity.activities.append(self)

    def __str__(self):
        '''Funcao para exibir o nome e a descricao da atividade'''
        return f'{self._title} | {self._description} | {self._time}'

    @classmethod
    def list_activities(cls):
        '''Funcao para listar as atividades'''
        print(f'{'Activity'.ljust(25)} | {'Description'.ljust(25)} | {'Time'.ljust(25)}')
        for activity in cls.activities:
            print(f'{activities._title.ljust(25)} | {activities._description.ljust(25)} | {str(activities.time).ljust(25)}')
