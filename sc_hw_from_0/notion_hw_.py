# 1) Напишите программу, которая ждет от пользователя имя(name).
# Далее, требуется распечатать фразу “Hello, my friend ” + name, пять
# раз. Нельзя использовать функцию print() более одного раза.

# 2) Устройте небольшой опрос пользователю. Задайте такие вопросы:
# -” Как вас зовут?”
# -” Сколько вам лет?”
# -” Где вы учитесь/работаете?”
# -” Какая сфера IT вас интересует?”
# -” На каком языке вы программируете?”
# Ответы на эти вопросы нужно будет сохранить в переменные. После
# чего, нужно распечатать:
# “Имя: ...”,
# “Возраст: ...”,
# “Место учебы: ...”, и так далее, используя форматирование
# строк(format).

# 3) Создайте программу которое ждет строку, она должна высчитать
# длину строки, то есть посчитать количество букв, и вывести эту
# строку столько же раз, сколько букв в ней.

# 4) Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево.

# 5) Выведите первый и последний элемент строки.

# 6) Есть переменная number содержащая данное значение
# “123456789”, измените переменную с помощью slice(среза) так,
# чтобы после распечатки, выходило “13579” и “2468”.

# # 1 
# name = input('wats ur name?: ').capitalize()
# surname  = input(f'whats ur surname {name}: ').capitalize()
# print(f'hello my friend {name} {surname}')


# while True:
#     name = input('enter name :')
#     if name == 'done':
#         break
#     surname = input(f'ok {name} neter surname: ')
#     if surname == 'done':
#         break
#     else:
#         print(f'nice to meat you {name} {surname}')
#         continue

name = 'John'
surname = 'Nash'
company = 'Google sdbfb sdjgutngik eyvgsydvbjf ihnihnfkuby  jnfgjnkg'
# print(name.encode())
# print(surname.encode())
# company = company.split()               # ['Google', 'sdbfb', 'sdjgutngik', 'eyvgsydvbjf', 'ihnihnfkuby', 'jnfgjnkg']
# company = company.splitlines()          # ['Google sdbfb sdjgutngik eyvgsydvbjf ihnihnfkuby  jnfgjnkg']
# company = company.startswith('G')       # True
# company = company.endswith('g')         # True    
# print(company[-1])

# print(company)
# # word = input('enter word: ')


# x1 = int(input('Введите координату x1: '))
# x2 = int(input('Введите координату y1: '))
# y1 = int(input('Введите координату x2: '))
# y2 = int(input('Введите координату y2: '))
# if x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
#     print('YES')
# else:
#     print('NO')



# print("mark" > "Mark")     # True
"""
# ord()
"""
"""
print(ord('M'))
print(ord('m'))

"""
# >>>"mark" > "Mark"
# True
# >>> ord('M')
# 77
# >>> ord('m')
# 109
# >>>
# my_list = [1, 2, 3, 4, 5]
# my_list.insert(1,'Привет')
# print(my_list)              # [1, 'Привет', 2, 3, 4, 5]


# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# list_2  =  ['шесть',  'семь']
# my_list.extend(list_2)
# print(my_list)                  # ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь']

# my_list = ['один', 'два', 'три', 'четыре', 'пять']
# del my_list[1:3]      
# print(my_list)                  # ['один', 'четыре', 'пять']

# all_fruits = ['Apple', 'Grape', 'Peach', 'Banan', 'Orange']
# my_favorite_fruits = ['Apple', 'Banan', 'Orange']

# for i in all_fruits:
#     if i in my_favorite_fruits:
#         print(i + ' is my favorite fruit')
#     else:
#         print('I do not like ' + i)


# list.sort([key=функция])  # Сортирует список на основе функции

# заменим каждый пятый символ предложения, начиная с 0-го, на *

# for i in range(text):
#     if i[0] % 5 == 0:
#         new_text += '*'
#     else:
#         new_text += i[1]
#     print(new_text)


# print(text.replace(' ','-'))                 # Это-не-те-дроиды,-которых-вы-ищете






# text = "Это не те дроиды, которых вы ищете"
# new_text = ""

# for i in enumerate(text):
#     if i[0] % 5 == 0:
#         new_text += '*'
#     else:
#         new_text += i[1]    
# print(new_text)                               # *то н* те *роид*, ко*орых*вы и*ете


# nnn = ''

# for i in enumerate(company):
#     if i[0] % 6 == 0:
#         nnn += '%'
#     else:
#         nnn += i[1]
# print(nnn)



# chu_chu = 'biz hozir enumirate ishga tushuramiz'
# pust = ''

# for i in enumerate(chu_chu):
#     if i[0] %5 == 0:
#         pust += '.|.'
#     else:
#         pust += i[1]
# print(pust)


# nert = [1,2,3,4,5,6,7,8,9,10]           
# sttr = ''

# for i in nert:
#     sttr += str(i)
#     print(sttr)                                  

# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567
# 12345678
# 123456789
# 12345678910


# for i in nert:
#     sttr += str(i)
# print(sttr)                                  

# 12345678910



# # count
# count = 0
# for i in company:
#     count += 1
# print(count)

# # break
# for i in range(0, 50):
#     if i == 22:
#         break
#     print(i)                  # start 1...21 end

# # continue
# for a in range(1, 20):
#     if a == 10:
#         continue
#     print(a)                  # start ...8,9,11,12..... end



# strange_phonebook = [["Alex", "Andrew", "Aya", "Azazel"],["Barry", "Bill", "Brave", "Byanka"],["Casey", "Chad", "Claire", "Cuddy"],["Dana", "Ditrich", "Dmitry", "Donovan"]]
# # это список списков, где каждый подсписок состоит из строк
# # следовательно можно (зачем-то) применить тройной for
# # для посимвольного чтения всех имён
# # и вывода их в одну строку
# for first in strange_phonebook:
#     for second in first:
#         for third in second:
#             print(third, end=' ')







# # Цикл по словарю
'''
.items()

'''
# Чуть более сложный пример связан с итерированием словарей. Обычно, при переборе словаря, нужно получать и ключ и значение. Для этого существует метод `.items()`, который создает представление в виде кортежа для каждого словарного элемента.

# Цикл, в таком случае, будет выглядеть следующим образом:


# # создадим словарь
# top_10_largest_lakes = {
#     "Caspian Sea": "Saline",
#     "Superior": "Freshwater",
#     "Victoria": "Freshwater",
#     "Huron": "Freshwater",
# }

# # обойдём его в цикле for и посчитаем количество озер с солёной водой и количество озёр с пресной
# salt = 0
# fresh = 0
# # пара "lake, water", в данном случае, есть распакованный кортеж, где lake - ключ словаря, а water - значение.# цикл, соответственно, обходит не сам словарь, а его представление в виде пар кортежей

# for lake, water in top_10_largest_lakes.items():
# 	if water == 'Freshwater':
#         fresh += 1
# else:
#     salt += 1
# print("Amount of saline lakes in top10: ", salt)
# print("Amount of freshwater lakes in top10: ", fresh)

# # > Amount of saline lakesin top10:  1
# # > Amount of freshwater lakesin top10:  3





stribg = """Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."""


# print(stribg.lower().replace('advert', 'ADVERT'))

a = 'adilet'
b = 'aidana'
a = a.capitalize()
b = b.capitalize()
print(len(a))
print(len(b))

print(b[0]+a[0]+b[1]+a[1]+b[2]+a[2]+b[3]+a[3]+b[4]+a[4]+b[5]+a[5])



aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

#  Получите из кортежа число 20 и запишите в отдельную переменную

res = aTuple[1][1]
print()


