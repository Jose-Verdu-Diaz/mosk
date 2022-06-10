import datetime as dt

from lib.gui import Clr

class Task():

    def __init__(self, **kwargs) -> None:
        if kwargs['importance'] not in list(range(6)): raise ValueError(f'Importance must be between 0 and 5 (inclusive). Value found: {kwargs["importance"]}.')

        self.name = kwargs['name']
        self.description = kwargs['description']
        self.tasks = []
        if kwargs['selected_task'] == None: self.level = 0
        else: self.level = len(kwargs['selected_task'])
        self.importance = kwargs['importance']
        self.completed = False
        self.creation = dt.datetime.now()
        

    def new_task(self, **kwargs):
        if len(kwargs['selected_task']) - 1 == self.level: self.tasks.append(Task(**kwargs))
        else: self.tasks[kwargs['selected_task'][self.level]].new_task(**kwargs)


    def name_str(self):
        clr = Clr()
        imp_clr = ['', clr.CYAN, clr.GREEN, clr.YELLOW, clr.RED]
        
        txt = self.name if self.completed else f'{self.name} ⬤ {clr.ENDC}'
        if self.tasks: txt = f'▴ {txt}'
        for l in range(self.level + 1): txt = f'\t{txt}'

        ret = f'{clr.STRIKETHROUGH}{clr.GREY}{txt}' if self.completed else f'{imp_clr[self.importance]}{txt}'
        return ret

