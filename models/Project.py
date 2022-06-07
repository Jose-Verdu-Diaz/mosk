import pickle as pkl

class Project:

    def __init__(self, name:str, description:str=None) -> None:
        self.name = name
        self.description = description
        self.tasks = None

        self.save()

    def save(self):
        with open(f'data/projects/{self.name}.pkl', 'wb') as f: pkl.dump(self, f)