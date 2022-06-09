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


    def project_info(self, **kwargs):
        total = []
        for i, l in enumerate(kwargs['selected_task']):
            if i == 0: total.append(self.tasks)
            else: total.append(total[-1][l].tasks, l)

        #TODO: Display subtasks

        info = {
            'name': self.name,
            'description': self.description,
            'tasks': task_list
        }
        return info


    def new_task(self, **kwargs):
        if kwargs['selected_task'] == None:
            input('You are adding a task at level 0')
            self.tasks.append(Task(**kwargs))
        else:
            input('You are adding a task at a deeper level')
            self.tasks[kwargs['selected_task'][0]].new_task(**kwargs)

        self.save()


    def complete_task(self, task_id):
        self.tasks[task_id].completed = not self.tasks[task_id].completed
        self.save()