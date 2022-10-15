# 1
for i in range(1,6):
    print(str(i)+'-'+'0')

# 2
count = 0
for su in range(1,100):
    count += su
print(count)


# 3
while 1:
    num1 = int(input(': '))
    num2 = int(input(': '))
    num3 = int(input(': '))

    if num1 == num2 or num1 == num3 or num2 == num3:
        print('yes')
    else:
        print('no')
        
# 4
while 1:
    n1 = int(input(': '))
    n2 = int(input(': '))
    n3 = int(input(': '))

    if n1 + n2 == n3 or n3 + n1 == n2 or n2 + n3 == n1:
        print('yes')
    else:
        print('no')


# 5
a = input(': ')
b = input(': ')
c = input(': ')

print(f'{3-(a+b+c).count("-")}')


# 6
for s in range(1, 497):
    if s % 2 == 0:
        print(s)


# 7
count = 1
for u in range(1,15):
    count += u
print(count)



# 8
count = 1
for v in range(0,9435):
    count += v
print(count)



# 9
for x in range(54,9184):
    x = x * 5
    print(x)


# 10

while 1:
    print('\npush the (Ctrl + z) for breaking program')
    a_1 = int(input('enter n1: '))
    b_1 = int(input('enter n2: '))
    ub = []
    vz = []

    if b_1 > a_1:
        for voz in range(a_1, b_1 + 1):
            vz.append(voz)
        print(vz)
        print('po vozrastaniyu')
    else:
        for ubv in range(b_1, a_1 + 1):
            ub.append(ubv)
        print(ub[::-1])
        print('po ubivaniu')



# 11

# Мы уже с Вами знаем что такое факториал. Вводим переменную a. Выведите значение a!


