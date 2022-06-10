import pickle as pkl
import time

from lib.gui import Clr
from lib.utils import flatten_list
from models.Task import Task

class Project:

    def __init__(self, name:str, description:str=None) -> None:
        self.name = name
        self.description = description
        self.tasks = []

        self.save()


    def save(self):
        with open(f'data/projects/{self.name}.pkl', 'wb') as f: pkl.dump(self, f)


    def list_tasks(self, **kwargs):
        selected_task = kwargs['selected_task']

        total = []
        for i, l in enumerate(selected_task):
            if i == 0: total.append(self.tasks)
            else: total.append(total[-1][selected_task[i - 1]].tasks)

        task_joined = total[0]
        for i in range(len(selected_task)): 
            if i == 0: continue
            task_joined.insert(selected_task[i - 1] + 1, total[i])

        result_list = flatten_list(task_joined)

        return result_list


    def selected_task(self, **kwargs):
        selected_task = kwargs['selected_task']
        total = self.list_tasks(**kwargs)
        total = flatten_list(total)

        for i, idx in enumerate(selected_task):
            if i == 0: task_idx = idx
            else: task_idx += idx + 1

        return total[task_idx]


    def project_info(self, **kwargs):
        task_list = []
        for t in self.list_tasks(**kwargs): task_list.append(t.name_str())

        info = {
            'name': self.name,
            'description': self.description,
            'tasks': task_list
        }
        return info


    def new_task(self, **kwargs):
        selected_task = kwargs['selected_task']
        if selected_task == None: self.tasks.append(Task(**kwargs))
        else: self.tasks[selected_task[0]].new_task(**kwargs)

        self.save()


    def complete_task(self, task_id):
        self.tasks[task_id].completed = not self.tasks[task_id].completed
        self.save()