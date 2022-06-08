import os

from lib.input import inp_str, inp_int
from lib.gui import banner, main_menu, clear, new_menu, new_project, projects_menu, project_info
from models.Project import Project
from models.State import State


def main():
    state = State()

    # Main Menu
    while True:
        print_list = [clear, banner, main_menu]
        for p in print_list: p()
        inp = inp_str(options=['e', 'p', 't', 'i', 'n'])
        if inp == None: continue
        elif inp == 'e': break

        # Projects
        elif inp == 'p':
            while True:
                kwargs = {'project_names':state.prj_list()}
                print_list[-1] = projects_menu
                for p in print_list: p(**kwargs)
                inp = inp_int(options=list(range(len(state.projects))))
                if inp == None: continue
                elif inp == 'e': break

                # Project Info
                else:
                    kwargs = {'project_info':state.projects[inp].project_info()}

                    while True:
                        print_list[-1] = project_info
                        for p in print_list: p(**kwargs)
                        inp = inp_str(options=['e'])
                        if inp == None: continue
                        elif inp == 'e': break

        # Incubator
        elif inp == 'i':
            pass

        # Create New
        elif inp == 'n':
            while True:
                print_list[-1] = new_menu
                for p in print_list: p()
                inp = inp_str(options=['e', 'p', 't'])
                if inp == None: continue
                elif inp == 'e': break

                # Create New Project
                elif inp == 'p':
                    kwargs = {
                        'name':'',
                        'description':''
                    }
                    while True:
                        print_list[-1] = new_project
                        for p in print_list: p(**kwargs)
                        inp = inp_str(options=['e', 'c', 'n', 'd'])
                        if inp == None: continue
                        elif inp == 'e': break

                        # Create New Project: Name
                        elif inp == 'n': kwargs['name'] = inp_str(prompt='Enter name: ')

                        # Create New Project: Description
                        elif inp == 'd': kwargs['description'] = inp_str(prompt='Enter description: ')

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