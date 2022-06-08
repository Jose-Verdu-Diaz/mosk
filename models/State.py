import os
import pickle as pkl

from models.Project import Project

class State:

    def __init__(self) -> None:
        self.projects = []
        self.tasks = []
        self.incubator = []

        for f in os.listdir('data/projects'):
            with open(f'data/projects/{f}', 'rb') as file: self.projects.append(pkl.load(file))
        for f in os.listdir('data/tasks'):
            with open(f'data/tasks/{f}', 'rb') as file: self.tasks.append(pkl.load(file))
        for f in os.listdir('data/incubator'):
            with open(f'data/projects/{f}', 'rb') as file: self.incubator.append(pkl.load(file))


    def prj_list(self):
        return [f'({i}): {p.name}' for i, p in enumerate(self.projects)]

    
    def new_project(self, **kwargs):
        self.projects.append(Project(**kwargs))