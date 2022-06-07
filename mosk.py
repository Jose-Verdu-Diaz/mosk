from operator import ge
from lib.input import inp_char
from lib.gui import banner, main_menu, clear, new_menu

def main():

    while True:
        print_list = [clear, banner, main_menu]
        for p in print_list: p()

        inp = inp_char(options=['e', 'p', 'i', 'n'])
        if inp == None: continue
        if inp == 'e': break

        elif inp == 'n':
            print_list= [clear, banner, new_menu]
            while True:
                for p in print_list: p()

                inp = inp_char(options=['e', 'p', 't'])
                if inp == None: continue
                if inp == 'e': 
                    print_list.pop()
                    break

        else: print(inp)

if __name__ == '__main__':
    main()