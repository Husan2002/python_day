'''
 сделать программу которая спрашивает у пользователя действия,
 1 е действие - это добавление нового номера(имя и номер)
 2 е действие - это удаление существующего номера
 3 е действие - это поиск контакта по имени
 4 е действие - это вывод всех контактв

'''
spisok = []

class Contacts():
    global spisok
    global delit
    def ad_contact():
        global spisok
        spisok = []
        while 1:
            print('\nfor breakking program enter (done)')
            add_contact = input('please add contact: ')
            if add_contact == 'done':
                break
            spisok.append(add_contact)
            print(spisok)

    ad_contact()


    def show_contact():
        print(spisok)

    show_contact()

    
    def del_contact():
        global delit
        while 1:
            delit = input('enter name for delit contact: ')
            if delit == 'done':
                break
            spisok.remove(delit)
            print(spisok)
        print(spisok)
    del_contact()

