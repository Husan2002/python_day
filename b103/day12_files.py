# f = open('users.txt', 'a', encoding='utf-8')
# print(f)
# f.close()
# 
# file = open('users.txt', 'a', encoding='utf-8')
# file.write('hello aruuke\n')
# 
# f = open('users.txt', 'r', encoding='utf-8')
# ff = f.read()
# print(ff)


name_surname_thirdname = input('enter name,surname,patronymic please: ')
birth_year = int(input('Enter birth year: '))
location = input('enter name please: ')
phone_number = int(input('enter phone_number of student: '))

while 1:
    print('1.add\n2.exit\n: ')
    usl = int(input('FIO: '))
    if usl == '1':
        name = input('FIO: ').title()
        if ' ' in name:
            first_name = name.split()[0]
            second_name = name.split()[1]
            if len(first_name) > 2 and len(second_name) > 3:
                try:
                    phone = int(input('telefon: '))
                    if len(str(phone)) > 9 or len(str(phone)) <= 12:
                        try:
                            birth_year = int(input('Enter birth year: '))
                            if birth_year > 1930 and birth_year < 2023:
                                location = input('enter location please: ')
                                if len(location) > 3:
                                    lst = [name, phone_number, birth_year, location]
                                else:
                                    print('enter correct location please..!')
                                    continue
                            else:
                                print('WTF..? -_-')
                                continue
                        except ValueError:
                            print('this value most be a number')
                            continue
                    else:
                        print('enter all number')
                        continue
                except ValueError:
                    print('this value most be number')
                    continue
                print(lst)
                with open('users.txt', 'a', encoding='utf-8') as f:
                    print(*lst, file = f)
    elif usl == 2:
        break


