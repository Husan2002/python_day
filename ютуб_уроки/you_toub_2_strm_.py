# num = int(input('enter lnumber: '))
# k = 0
# lst = []
# for i in range(1, num +1):
#     if num % i == 0:
#         k+=1
#         lst.append(i)
# if k == 2:
#     print('prostoe chislo')
# else:
#     print('neprostoe chislo')
#     print(lst)


a = int(input('enter number: '))
s = 0

while a > 0:
    s += a % 10
    s = a // 10

print(s)