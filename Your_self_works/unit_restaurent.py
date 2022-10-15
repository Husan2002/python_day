from Menu_ import MENU_YS




name = input('nazavite svoe imya: ').capitalize()

print(f'Dobro pojalovat {name} na nash resstaran Classic\n              Menu')


while 1:
    vibor_menu = input('1.Napidki\n2.Salad\n3.Bluda\n4.Desert\n5.Quit\n: ')

    if vibor_menu == '1':
        print(MENU_YS.menu_drinks())
    elif vibor_menu == '2':
        print(MENU_YS.menu_salad())
    elif vibor_menu == '3':
        print(MENU_YS.menu_bluda())
    elif vibor_menu == '4':
        print(MENU_YS.menu_disert())
    elif vibor_menu == '5':
        break

print('мы всегда вам рады приходите еще')