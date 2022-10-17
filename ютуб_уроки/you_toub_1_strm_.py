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



def scuare(a):
    p = a * 4
    s = a ** 2
    return p,s

print(scuare(10))
