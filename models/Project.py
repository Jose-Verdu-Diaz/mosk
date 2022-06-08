import pickle as pkl

from lib.gui import Clr
from models.Task import Task

class Project:

    def __init__(self, name:str, description:str=None) -> None:
        self.name = name
        self.description = description
        self.tasks = []

        self.save()


    def save(self):
        with open(f'data/projects/{self.name}.pkl', 'wb') as f: pkl.dump(self, f)


    def project_info(self):
        clr = Clr()
        info = {
            'name': self.name,
            'description': self.description,
            'tasks': [t.name_str() for t in self.tasks]
        }
        return info


    def new_task(self, **kwargs):
        self.tasks.append(Task(name=kwargs['name'], description=kwargs['description']))
        self.save()


    def complete_task(self, task_id):
        self.tasks[task_id].completed = not self.tasks[task_id].completed
        self.save()