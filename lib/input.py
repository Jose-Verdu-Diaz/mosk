def inp_str(prompt:str=None, options:list=None):
    try: 
        if not prompt: prompt = 'Enter an option: '
        inp = input(prompt)
    except Exception: input('Unexpected input. Press Enter to continue...')

    if options: 
        if inp not in options: 
            input(f'The string should be one of the following: {options}. Press Enter to continue...')
            return None

    return inp


def check_int(inp, options:list=None):
    try: inp = int(inp)
    except Exception: 
        return None

    if options: 
        if inp not in options: 
            input(f'The string should be one of the following: {options}. Press Enter to continue...')
            return None

    return inp


def inp_int(prompt:str=None, options:list=None, exit=True):
    try: 
        if not prompt: prompt = 'Enter an option: '
        inp = input(prompt)
    except Exception: 
        input('Unexpected input. Press Enter to continue...')
        return None

    if exit: 
        if inp == 'e': return inp

    check_int(inp, options)