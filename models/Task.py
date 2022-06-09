import datetime as dt

from lib.gui import Clr

class Task():

    def __init__(self, **kwargs) -> None:
        if kwargs['importance'] not in list(range(6)): raise ValueError(f'Importance must be between 0 and 5 (inclusive). Value found: {kwargs["importance"]}.')

        self.name = kwargs['name']
        self.description = kwargs['description']
        self.tasks = []
        self.level = 0
        self.importance = kwargs['importance']
        self.completed = False
        self.creation = dt.datetime.now()

        input(F'IMPORTANCE: {self.importance}')

    def add_task(self, name:str, description:str=None):
        self.tasks.append(Task(name, description, self.level + 1))

    def name_str(self):
        clr = Clr()
        imp_clr = ['', clr.CYAN, clr.GREEN, clr.YELLOW, clr.RED]

        ret = f'{clr.STRIKETHROUGH}{clr.GREY}{self.name}{clr.ENDC}' if self.completed else f'{imp_clr[self.importance]}{self.name} ⬤ {clr.ENDC}'
        return ret

