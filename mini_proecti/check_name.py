class Name():
    def ch_name():
        list1 = ['husan','hasan','aziz','artur','kishi','hotin']
        while 1:
            name = input('enter name:')
            if name == 'done':
                print('we hope you will back :)')
                break
            elif name in list1:
                print(f'yes {name}')
            else:
                print(f'who is this {name}')

    # ch_name()