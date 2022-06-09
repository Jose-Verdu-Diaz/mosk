import os
import sys
import time
from termios import tcflush, TCIFLUSH

from lib.keyboard import read_key, on_press_key
from lib.input import inp_str, inp_int
from lib.gui import Clr, banner, main_menu, clear, new_menu, new_project, new_task, projects_menu, project_info
from models.Project import Project
from models.State import State


def main():
    state = State()

    # Main Menu
    while True:
        print_list = [clear, banner, main_menu]
        for p in print_list: p()
        inp = read_key()
        if inp == None: continue
        elif inp == 'e': break

        # Projects
        elif inp == 'p':
            while True:
                kwargs = {'project_names': state.prj_list()}
                print_list[-1] = projects_menu
                for p in print_list: p(**kwargs)
                inp = inp_int(options=list(range(len(state.projects))))
                if inp == None: continue
                elif inp == 'e': break

                # Project Info
                else:
                    proj_id = inp
                    kwargs = {'selected_task': 0}
                    while True:
                        kwargs['project_info'] = state.projects[proj_id].project_info()
                        print_list[-1] = project_info
                        for p in print_list: p(**kwargs)

                        inp = read_key()
                        if inp == None: continue
                        elif inp == 'e': break

                        # Project Info New Task
                        elif inp == 'n':
                            kwargs['name'], kwargs['description'] = '', ''
                            while True:
                                print_list[-1] = new_task
                                for p in print_list: p(**kwargs)
                                inp = read_key()
                                if inp == None: continue
                                elif inp == 'e': break

                                # Project Info New Task: Name
                                elif inp == 'n':
                                    for p in print_list: p(**kwargs)
                                    kwargs['name'] = inp_str(prompt='Enter name: ')

                                # Project Info New Task: Description
                                elif inp == 'd':
                                    for p in print_list: p(**kwargs)
                                    kwargs['description'] = inp_str(prompt='Enter description: ')

                                # Project Info New Task: Create
                                elif inp == 'c':
                                    state.projects[proj_id].new_task(**kwargs)
                                    break

                        elif inp == 'c': 
                            state.projects[proj_id].complete_task(kwargs['selected_task'])
                            kwargs['project_info'] = state.projects[proj_id].project_info()

                        elif inp == 'i': 
                            state.projects[proj_id].complete_task(kwargs['selected_task'])
                            kwargs['project_info'] = state.projects[proj_id].project_info()

                        elif inp == 'up':
                            if kwargs['selected_task'] > 0: 
                                kwargs['selected_task'] -= 1
                        elif inp == 'down':
                            if kwargs['selected_task'] < len(state.projects[proj_id].tasks) - 1: 
                                kwargs['selected_task'] += 1

        # Incubator
        elif inp == 'i':
            pass

        # Create New
        elif inp == 'n':
            while True:
                print_list[-1] = new_menu
                for p in print_list: p()
                inp = read_key()
                if inp == None: continue
                elif inp == 'e': break

                # Create New Project
                elif inp == 'p':
                    kwargs = {
                        'name': '',
                        'description': ''
                    }
                    while True:
                        print_list[-1] = new_project
                        for p in print_list: p(**kwargs)
                        inp = read_key()
                        if inp == None: continue
                        elif inp == 'e': break

                        # Create New Project: Name
                        elif inp == 'n':
                            for p in print_list: p(**kwargs)
                            kwargs['name'] = inp_str(prompt='Enter name: ')

                        # Create New Project: Description
                        elif inp == 'd': 
                            for p in print_list: p(**kwargs)
                            kwargs['description'] = inp_str(prompt='Enter description: ')

                        # Create New Project: Create
                        elif inp == 'c':
                            state.new_project(**kwargs)
                            break
                    del kwargs
                            
                # Create New Task
                elif inp == 'p':
                    pass

        else: print(inp)


if __name__ == '__main__':
    if not os.path.isdir('data/projects'): os.makedirs('data/projects')
    if not os.path.isdir('data/tasks'): os.makedirs('data/tasks')
    if not os.path.isdir('data/incubator'): os.makedirs('data/incubator')
    main()