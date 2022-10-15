# # 1)Создать функцию calc(a, b, operation). Описание входных параметров:
# # Первое число(дробное число)
# # Второе число(дробное число)
# # Действие над ними:
# #    1) + Сложить
# #    2) - Вычесть
# #    3) * Умножить
# #    4) / Разделить
# #    Сделайте момент где если пользователь делит число на 0, нужно вывести “На    ноль делить нельзя”
# #    В остальных случаях функция должна возвращать "Операция не поддерживается"

# def calc():
#     while True:
#         print('')
#         print('for breakking program ente (done)')
#         print('')
#         sign = input('+ - * /\nenter sign: ')
#         if sign == 'done':
#             break
#         n1 = None
#         n2 = None
        
#         if sign in ('+','-','*','/'):
            
#             while True:    
#                 n1 = input('enter number1: ')
#                 try:
#                     n1 = float(n1)
#                     break
#                 except ValueError:
#                     print('this value most be a number')
#                     continue                  
            
#             while True:
#                 n2 = input('enter number2: ')
#                 try:
#                     n2 = float(n2)
#                     break
#                 except ValueError:
#                     print('this value most be a number')
#                     continue
#         else:
#             print('enter correct value!')
#             continue

#         if sign == '+':
#             print('your answer',n1 + n2)
#         elif sign == '-':
#             if n1 - n2 < 0:
#                 print('your answer lower than zero..!',n1 - n2)
#             else:
#                 print('your answer',n1 - n2)
#         elif sign == '*':
#             print('your answer',n1 * n2)
#         elif sign == '/':
#             if n1 == 0 or n2 == 0:
#                 print('devision by zero...!')
#             else:
#                 print('your answer',n1 / n2)
#     print('we hope you will back :)')

# # calc()


# # 2)Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139

# for i in range(201):
#     if i % 2 != 0:
#         if i == 139:
#             break
#         print(i)



# # 3)Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный(то есть 29 февраль в календаре), и False иначе.

# def is_year_leap(year):
#     year = int(input())
#     if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
#         return False
#     else:
#         return True

# is_year_leap()


# # 4)Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

# def square(argument):
#     p = argument * 4
#     s = argument * argument
#     d = (argument ** argument) / 2
#     d = d ** 0.5

#     k = (p,s,d)
#     return k

# print(square(32))


# # 5)Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# # Написать функцию bank, принимающая аргументы money и years, и возвращающую сумму, которая будет на счету пользователя.

p = int(input())
x = int(input())
y = int(input())
 
pr1 = x/100*p
 
res = x+pr1
 
res2 = str(res).replace('.', ' ')
 
print(res2)




# # 6)Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

# def is_prime():
#     for i in range(1,1000):
#         if is_prime(i):
#             return True
#         else:
#             False
# is_prime()


# # 7)Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре(День от 1 до 30, месяц от 1 до 12, год от 0 до 2022), и  иначе False.



# # 8)Напишите функцию где дан список целых чисел. Посчитать, сколько раз в нем встречается каждое число. Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза, число 3 - два раза, числа 2 и 4 - по одному разу.
# # Подсказка: можно использовать цикл for и метод count

# def count_in_lst():    
#     lst1 = [1, 1, 3, 2, 1, 3, 4]
#     while 1:
#         num = int(input('enter numbee: '))
#         count = 0

#         for i in lst1:
#             if num == i:
#                 count += 1
#             elif num != i:
#                 pass
#             else:
#                 print('it doesn\'t have in list')
#         print(count)


# count_in_lst()


