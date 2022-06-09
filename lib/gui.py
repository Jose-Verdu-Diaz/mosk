import os

class Clr:

    def __init__(self):
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m'
        self.BLUE = '\033[34m'
        self.PURPLE = '\033[35m'
        self.CYAN = '\033[36m'
        self.GREY = '\033[90m'

        self.ENDC = '\033[m'
        self.BOLD = '\033[01m'
        self.UNDERLINE = '\033[04m'
        self.REVERSE = '\033[07m'
        self.STRIKETHROUGH = '\033[09m'


def clear(**kwargs):
    os.system('cls' if os.name == 'nt' else 'clear')


def banner(**kwargs):
    banner ='''
    8b    d8  dP"Yb  .dP"Y8 88  dP 
    88b  d88 dP   Yb `Ybo." 88odP  
    88YbdP88 Yb   dP o.`Y8b 88"Yb  
    88 YY 88  YbodP  8bodP' 88  Yb 

    '''
    print(f'{Clr().CYAN}{banner}{Clr().ENDC}')


def main_menu(**kwargs):
    print_list = [
        '(e)xit',
        '(p)rojects',
        '(t)asks',
        '(i)ncubator',
        '(n)ew'
    ]
    print('Main:')
    for p in print_list: print(f'\t{p}')
    print('\n')


def projects_menu(project_names):
    project_names = project_names.copy()
    project_names.insert(0, '(e)xit\n')
    print('Projects:')
    for p in project_names: print(f'\t{p}')
    print('\n')


def project_info(**kwargs):
    clr = Clr()
    project_info, selected_task = kwargs['project_info'], kwargs['selected_task']
    project_info = project_info.copy()
    print_list = [f'Name: {project_info["name"]}']
    print_list.append(f'Description: {project_info["description"]}')
    print_list.append(f'Tasks:')
    if len(project_info['tasks']):
        print_list.extend([f'\t{clr.REVERSE}{t}{clr.ENDC}' if i == selected_task  else f'\t{t}' for i, t in enumerate(project_info['tasks'])])
    print('(e)xit | (n)ew task | (c)omplete task | change (i)mportance\n')
    print('Project Info:')
    for p in print_list: print(f'\t{p}')
    print('\n')


def new_menu(**kwargs):
    print_list = [
        '(e)xit',
        '(p)roject',
        '(t)ask'
    ]
    print('New:')
    for p in print_list: print(f'\t{p}')
    print('\n')


def new_project(**kwargs):
    data = {
        '(n)ame: ': kwargs['name'],
        '(d)escription: ': kwargs['description']
    }
    print_list = [f'{d}{data[d]}' for d in data]
    print_list.insert(0, '(c)reate\n')
    print_list.insert(0, '(e)xit')
    print('New Project:')
    for p in print_list: print(f'\t{p}')
    print('\n')


def new_task(**kwargs):
    clr = Clr()
    data = {
        '(n)ame: ': kwargs['name'],
        '(d)escription: ': kwargs['description']
    }
    imp_clr = ['', clr.CYAN, clr.GREEN, clr.YELLOW, clr.RED]
    imp_str = " ".join([f"{clr.REVERSE}{imp_clr[i]}{i}{clr.ENDC}" if kwargs["importance"] == i else f'{imp_clr[i]}{i}{clr.ENDC}' for i in range(5)])
    print_list = [f'{d}{data[d]}' for d in data]
    print_list.append(f'Importance: {imp_str}')
    print_list.insert(0, '(c)reate\n')
    print_list.insert(0, '(e)xit')
    print('New Task:')
    for p in print_list: print(f'\t{p}')
    print('\n')