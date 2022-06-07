def inp_char(options:list = None):
    try: inp = input('Enter an option: ')
    except Exception: input('Unexpected input. Press Enter to continue...')

    if options: 
        if inp not in options: 
            input(f'The character should be one of the following: {options}. Press Enter to continue...')
            return None

    return inp