import pickle as pkl

class Project:

    def __init__(self, name:str, description:str=None) -> None:
        self.name = name
        self.description = description
        self.tasks = None

    def save(self):
        with open(f'data/{self.name}.pkl', 'wb') as f: pkl.dump(self)