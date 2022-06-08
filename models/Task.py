class Task():

    def __init__(self, name:str, description:str=None, level:int=0, importance:int=0) -> None:
        if importance not in list(range(6)): raise ValueError('Importance must be between 0 and 5 (inclusive).')

        self.name = name
        self.description = description
        self.tasks = []
        self.level = level
        self.importance = importance
        self.completed = False

    def add_task(self, name:str, description:str=None):
        self.tasks.append(Task(name, description, self.level + 1))

