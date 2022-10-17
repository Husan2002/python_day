# x = [int(a) for a in input().split()]
# print(x)

# for i in input('enter number: '):
    # print(int(i))

"""max and min values
"""

# a,b,c = int(input('enter number: ')),int(input('enter number: ')),int(input('enter number: '))

# x = a if a > b and a > c else b if b > c else c
# y = a if a < b and a < c else b if b < c else c

# print(x,y)

"""как найти весакосный год
"""

# year = int(input('enter year: '))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f'{year} весакосный год')
# else:
#     print(f'{year} невесакосный год')

"""как найти пириметр и площядь квадрата
"""

# def scuare(a):
#     print(f'pirimetr kvadrata so storonoy {a} yavlaetsa {a * 4}')
#     print(f'ploshad kvadrata yavlaetsa {a ** 2}')
    

# scuare(int(input('enter number: ')))

"""среднее арефметическое число
"""

# summ = 0
# lenn = 0
# for i in range(1, 101):
#     if i %2 == 0:
#         summ += i
#         lenn += 1

# print(summ//lenn)

"""как найти максимальный елимент без встроенных функции 'max and min'
"""

mac = 1
for ma in range(1,101):
    if ma > mac:
        mac = ma
print(mac)

mic = 100
for mi in range(1,101):
    if mi < mic:
        mic = mi
print(mic)


# maxx = 1

# for i in range(1, 101):
#     if i % 3==0 and i % 2==0:
#         if i > maxx:
#             maxx = i
    
# print(maxx)



"""найти наибольший общий делитель
"""

a, b = int(input('enter number ')),int(input('enter number '))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

print(a + b)