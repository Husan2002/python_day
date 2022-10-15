# Всем привет! Тут есть 9 примеров и вы должны их перевести в тернарный оператор. Например: 

#-------------------Обычные уловия---------------------- 

# a, b = 22,5 
# if a > b: 
#     print("Python") 
# else: 
#     print("No python") 

#------------------------Тернарный оператор--------------------------- 

a, b = 22,5 
res = "Python" if a > b else "No python" 
# print(res) 
a, b, c = 14, 24, 5 

max = a if a > b and a>c else b if b > c else c 
# print(max) 

# 1) 

# age = int(input("Возраст: ")) 
# if age >= 18 and age <= 50: 
#     print("Доступ разрешен") 
# elif age > 50: 
#     print("Вы уже старый") 
# else: 
#     print("Иди домой") 

# ------------------------Тернарный оператор--------------------------- 

# age = int(input("Возраст: ")) 
# print("Доступ разрешен" if age >= 18 and age <= 40 else "Иди домой" if age > 50  else "Вы уже старый")


# 2) 

my_passwords = ["qwerty", "12345678"] 
# user_input = input("Введите пароль: ") 
# if user_input in my_passwords: 
#     print("Пароль верный") 
# else: 
#     print("Неверный пароль") 

# ------------------------Тернарный оператор---------------------------

# print("Пароль верный" if user_input in my_passwords else "Неверный пароль")

# 3) 

# number = int(input("Пожалуйста ведите цифру: ")) 
# if number % 2 == 0: 
#     types = 'четным' 
# else: 
#     types = 'нечетным' 
# print(f'Ваша цифра {number} является {types} .')

# ------------------------Тернарный оператор---------------------------
# types = 'четным' if number % 2 == 0 else 'нечетным'
# print(f'Ваша цифра {number} является {types} .')


# 4)

boolean = True

# if boolean: 
    # boole = (f'{boolean} является истиной') 
# print(boole)

# ------------------------Тернарный оператор---------------------------

# print(f'{boolean} является истиной' if boolean == True else f'{boolean} является ложью')



# 5) 

# name = input("Ваше имя: ") 
names = ["Mark", "Kate", "Anna", "Smit"] 
# if name in names: 
#     print(f"{name} в нашем классе") 
# else: 
#     print(f"{name} не в нашем классе") 
# print(f"{name} в нашем классе" if name in names else print(f"{name} не в нашем классе")) 
# 6)
 
# lst = [] 
# for i in range(10): 
#     lst.append(i) 
# print(lst) 

lst = [i for i in range(10)]
# print(lst)

# 7) 

# lst = [] 
# for i in range(10): 
#     if i % 2 == 0: 
#         lst.append(i) 
# print(lst) 

lst2 = [i  for i in range(10) if i % 2 == 0]
# print(lst2)
# 8) 

cars = ["Bmw", "Mersedes", "Lexus", "Kia", "Lada"] 
# new_cars = []
# for x in cars: 
#     if "a" in x:
#         new_cars.append(x) 
# print(new_cars) 
new_cars = [x for x in cars if "a" in x]
# print(new_cars)
# 9) 

# squares = [] 
# for i in range(10): 
#     squares.append(i ** 2) 
# print(squares) 
squares = [i**2 for i in range(10)]
# print(squares)


# Если вы забыли что такое тернарный оператор или же забыли как писать тернарный код вот ссылка на notion: 
# https://island-farm-9b7.notion.site/Python-1-group-a8295f6fdd62414384ad8ae3ff57376e

