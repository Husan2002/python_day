# 1) Дано два числа. Вывести на экран наибольшее из чисел;

# 1.2) Проверка на отрицательные и положительные числа

# 1.5) Если вводится отрицательное число, перевести его в положительное

n1 = int(input('enter number: '))
n2 = int(input('enter number: '))

if n1 > n2:
    print(n1,'bolshe!')
    if n1 > 0 or n2 > 0:
        print('polojitelnoe chislo! ')
    elif n1 < 0 or n2 < 0:
        print('otretsatelnoe chislo! ')
elif n2 > n1:
    print(n2,'bolshe!')
    if n1 > 0 or n2 > 0:
        print('polojitelnoe chislo! ')
    elif n1 < 0 or n2 < 0:
        print('otretsatelnoe chislo! ')




# 2) Пользователь вводит два числа с клавиатуры. Вывести на экран yes, если они отличаются друг от друга, иначе вывести на экран No;

num_1 = int(input('enter num_1: '))
num_2 = int(input('enter num_2: '))
if num_1 == num_2:
    print('...Yes')
else:
    print('...No')


# 3) Дано число. Если оно больше 100 или меньше -100, то вывести на экран символ —, 
# иначе вывести на экран символ +;

our_n = int(input('neter number: '))

if our_n > 100 or our_n < -100:
    print('-')
else:
    print('+')


# 4) Пользователь вводит номер месяца (от 1 до 12). Вывести название сезона года на 
# экран (зима, весна, лето, осень);

while True:
    print('for brakking program enter incorrect Value..!')
    month_n = int(input('1 - 12\nenter month number: '))

    if month_n > 0 and month_n <= 2:
        print('зима',month_n)
    elif month_n >= 3 and month_n <= 5:
        print('весна',month_n)
    elif month_n >= 6 and month_n <= 8:
        print('лето',month_n)
    elif month_n >= 9 and month_n <= 11:
        print('осень')
    elif month_n == 12:
        print('зима',month_n)
    else:
        print('you number incorrect...!')
        break

# 5) Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes, иначе no
num1 = int(input('enter firs number: '))
num2 = int(input('enter second number: '))
num3 = int(input('enter third number: '))
if num1 > 10 and num2 > 10 and num3 > 10:
    print('Yes')
else:
    print('No')

# 6) Дано три числа. Найти количество положительных чисел среди них

number_1 = int(input('enter firs number: '))
number_2 = int(input('enter second number: '))
number_3 = int(input('enter third number: '))

list_for_c = []

if number_1 > 0:
    list_for_c.append(number_1)
else:
    print('enter correct Value...!')
if number_2 > 0:
    list_for_c.append(number_2)
else:
    print('enter correct Value...!')
if number_3 > 0:
    list_for_c.append(number_3)
else:
    print('enter correct Value...!')

print(len(list_for_c))


# 7) Пользователь вводит количество месяцев и лет. Вывести на экран количество дней 
# за это время. Считать, что в каждом месяце 29 дней;

moon_num = float(input('enter month number: '))
if moon_num > 0 and moon_num <= 12:
    print((moon_num)*30.42)
else:
    print('please enter month number..!')
    



# 8) Напишите программу которая принимает от пользователя цифру и присваивает ее переменной  first_num. Условие:
# 	а) если first_num делится на 3 и на 5 без остатков, выведите на экран "ого, делится"
# 	б) если first_num делится на 3 без остатка, то выведите на экран "арара"
# 	в) если first_num делится на 5 без остатка, то выведите на экран "огого" 


firs_num = int(input('enter number: '))
if firs_num % 3 == 0 and firs_num % 5 == 0:
    print('ого, делится')
elif firs_num % 3 == 0:
    print('apapa')
elif firs_num % 5 == 0:
    print('огого')
else:
    print("sory but this numer doesn't division by 3 or 5 ..!")


# 9) Напишите программу отбора в военкомат. Если Алмазу меньше 16ти лет то должно вывести 
# "еще рано", если 18 и выше то вывести "идем служить", 
# а если возраст равна 40 и выше то вывести "уже не надо"

army_age = int(input('please enter age: '))

if army_age > 0 and army_age <= 2:
    print('где твой памперс? ')
elif army_age > 2 and army_age < 7:
    print('позови старших?')
elif army_age >= 7 and army_age < 18:
    print('еще рано')
elif army_age >= 18 and army_age < 40:
    print('идем служить')
elif army_age >= 40 and army_age < 250:
    print('уже не надо')
elif army_age >= 250:
    print('так ты же здох :)')
else:
    print('enter age please!')