a = open("'hi_.py'", 'w')
a.write('kak tebya zovut?')
a.close()

a = open('hi_.py', 'r')
print(a.read())


with open('hi_.py', 'a') as f:
    f.write("' bugaga'")

a.close()


try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print('dicvision by zero..!')




# f = open('1.txt', 'r')
# print(f.read())
# f.close()

