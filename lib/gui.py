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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    banner ='''
    8b    d8  dP"Yb  .dP"Y8 88  dP 
    88b  d88 dP   Yb `Ybo." 88odP  
    88YbdP88 Yb   dP o.`Y8b 88"Yb  
    88 YY 88  YbodP  8bodP' 88  Yb 

    '''
    print(f'{Clr().CYAN}{banner}{Clr().ENDC}')

def main_menu():
    print_list = [
        '(e)xit',
        '(p)rojects',
        '(i)ncubator',
        '(n)ew'
    ]
    for p in print_list: print(f'\t{p}')
    print('\n')

def new_menu():
    print_list = [
        '(e)xit',
        '(p)roject',
        '(t)ask'
    ]
    print('New:')
    for p in print_list: print(f'\t{p}')
    print('\n')