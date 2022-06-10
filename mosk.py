import os
import sys
import time
from termios import tcflush, TCIFLUSH

from lib.keyboard import read_key
from lib.input import inp_str, inp_int, check_int
from lib.gui import Clr, banner, main_menu, clear, new_menu, new_project, new_task, projects_menu, project_info
from models.Project import Project
from models.State import State


def create_task(state, print_list, proj_id, selected_task):
    kwargs = {
        'name': '',
        'description': '',
        'importance': 0,
        'selected_task': selected_task
    }
    while True:
        print_list[-1] = new_task
        for p in print_list: p(**kwargs)
        inp = read_key()
        if inp == None: continue
        elif inp == 'e': break

        elif inp == 'left':
            if kwargs['importance'] > 0:
                kwargs['importance'] -= 1
        elif inp == 'right':
            if kwargs['importance'] < 4:
                kwargs['importance'] += 1

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
                inp = read_key()
                #inp = inp_int(options=list(range(len(state.projects))))
                if inp == None: continue
                elif inp == 'e': break

                else: 
                    inp = check_int(inp, options=list(range(len(state.projects))))
                    if inp == None: continue

                    # Project Info
                    else:
                        proj_id = inp
                        kwargs = {'selected_task': [0]}
                        while True:
                            kwargs['project_info'] = state.projects[proj_id].project_info(**kwargs)
                            print_list[-1] = project_info
                            for p in print_list: p(**kwargs)

                            inp = read_key()
                            if inp == None: continue
                            elif inp == 'e': break

                            # Project Info New Task
                            elif inp == 'n':
                                create_task(state, print_list, proj_id, None)

                            # Project Info: Complete Task
                            elif inp == 'c': 
                                state.projects[proj_id].complete_task(kwargs['selected_task'][-1])
                                kwargs['project_info'] = state.projects[proj_id].project_info()

                            # Project Info: Add Subtask
                            elif inp == 's': 
                                create_task(state, print_list, proj_id, kwargs['selected_task'])

                            # Project Info: Task up
                            elif inp == 'up':
                                if kwargs['selected_task'][-1] > 0:
                                    kwargs['selected_task'][-1] -= 1

                            # Project Info: Task down
                            elif inp == 'down':
                                if kwargs['selected_task'][-1] < len(state.projects[proj_id].selected_task(**kwargs).tasks) - 1: 
                                    kwargs['selected_task'][-1] += 1

                            elif inp == 'right':
                                if len(state.projects[proj_id].selected_task(**kwargs).tasks):
                                    kwargs['selected_task'].append(0)

                            elif inp == 'left':
                                if len(kwargs['selected_task']) > 1:
                                    kwargs['selected_task'].pop()


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