from Hw5_Todo_ import ToDo

print('Welcome to our program Todo')

name = input('what\'s your name: ').capitalize()

while 1:
    menu = int(input(f'Ok {name} choice the number\n1-rule\n2-watch list\n3-add actions\n4-remove actions\n5-Quit\n: '))
    if menu == 5:
        break
    elif menu == 1:
        print(ToDo.pravila())
    elif menu == 2:
        print(ToDo.prosmotr())
    elif menu == 3:
        print(ToDo.popolnenie())
    elif menu == 4:
        print(ToDo.udalenie())

print('We hope you will back :)')