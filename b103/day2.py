name = 'robert polson'

print(name[0], name[7])
print(name[0:6])
print(name[0:13:2])
print(name[::-1])


numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
chot = []
ne_chot = []

for i in numbers:
    if i % 2 != 0:
        ne_chot.append(i)
print(ne_chot)

for i in numbers:
    if i % 2 == 0:
        chot.append(i)
print(chot)
