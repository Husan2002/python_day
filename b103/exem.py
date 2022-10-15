# s = input('enter sign: ')
# a = int(input('enter number: '))
# b = int(input('enter number: '))

# try:
#     if s == '/':
#         print(a / b)

# except ZeroDivisionError:
#     print("Деление на ноль нельзя")

# print([i for i in range(20) if i % 2 == 0])



# def say_hello():
#     return 'Hello'

# def say_bye():
#     return 'Bye'

# from exem import say_hello

# print(say_hello())
# print(say_bye())



# У нас есть пустой словарь friends = {}. Запросить у пользователя Имя (ключ), Фамилию (значение) и добавить его в наш пустой словарь.


# name = input('enter name: ')
# surname = input('enter surname: ')
# friends = {name:surname}
# print(friends)


# log = input('enter login: ')
# pas = input('enter password: ')
# print('ok')
# lst = [log, pas]

# input_log = input('enter login: ')
# input_pas = input('enter password: ')

# if input_pas in lst and input_log in lst:
#     print("Добро пожаловать")
# else:
#     print("Логин или пароль неверный")


# def add (num1, num2):    
#     return num1 + num2 

# from exem import add
# print(add())



# strr = 'idot sneg'
# sss = 'idot sneg davno'

# strr = strr.split()
# sss = sss.split()
# print(sss[2],sss[1],sss[0])
# print(strr[1],strr[0])

# cars = ['BMW', 'Mercedes', 'Tesla', 'Volvo', 'Audi']
# count = 0
# for i in cars:
#     count += 1
#     print(f'{count}-{i}')



# print(round(673.3123))

# some_string = 'Mersedes'

# print(some_string[3:6])




# while True:
#     number = int(input("Введите сколько вам лет: "))
    
#     if number >= 18 and number < 50:
#         print('stop')
#         break
#     else:
#         continue




def sumer(*args):
    print(sum(args))

# sumer(34,55,22,76,11,87)

# def kw(**kwargs):
#     print(kwargs)


# kw(input(),input())



# def kw(**kwargs):
#     print(kwargs)

# kw(a = '1', b = '2', c = '3', d = '4')

print(globals())
