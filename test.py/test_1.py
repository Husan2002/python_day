# s = []
# for i in s:
#     s.append(0)
# print(len(s))          # 0

# dict1 = {'name':'Mike', 'salary': 80000}
# temp = dict1.pop('age')
# print(temp)              # Error

# a = []
# a += 'python'
# b = ['python']

# if a == b:
#     print(True)
# else:
#     print(False)         # KeyError: 'age'

# x = [10, [3.141, 20, [30, 'qqz', 2.718]], 'foo']
# 'как вывести "z" '
# z = x[1][2][1][2]
# print(z)                    

# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print(print(a[-6]))         #foo None

# b = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# print(b[4::-2])            # ['quux' , 'baz', foo']

# f = 420
# f1 = 69
# f2 = 228
# f, f1, f2 = f2, f, f1
# print(f, f1, f2)           # 228 420 69

# nums = [1, 2, 3, 4]
# x = 1

# for i in range(len(nums)):
#     x *= i
# print(x) # 0

# a = []
# a.append(a)
# print(a)     # [[...]]

# lst = [14, 7, 2]
# string = '{2}{1}{2}{0}'.format(lst[0], lst[1], lst[2])
# print(string)        # 27214

# x = [1, 2, 3]
# print(x in x)        # False

# a = not bool('False')
# if not a:
#     a = a + 1

# print(a)       # 1

# lst = [].append(5)
# print(lst)  # None

# print(type(1/2))      # <class ' float '>

# pi = 3.14
# print(f'{pi=}')      #pi=3.14

# x = True * 1

# if True + False:
#     False + True
#     print(x)
# else:
#     print(0)          # 1

# a = [1, 2, 3]
# b = a
# print(b[0], end='')
# a = [6, 7, 8]
# print(b[0], end='')    # 11


# a = [0, 2, -4, -2, 1]

# for i in a:
#     if i < 0:
#         a.append(abs(i))
#     x = i
# print(x)    # 2

# a, b, *c = [i for i in range(0, 16, 4) if i % 4 == 0]
# print(len(c))    # 2

# print(str(8/1**2**2) == str(8/2**2**1))       # False

# txt = 'AnyText'
# print(txt[-1::])     # t

# lst = [1,2,3,4]
# r = 1
# for i in range(len(lst)):
#     r*=i

# print(r)           # 0

# lst = [print(i) for i in range(100)]

# liss = []    
# for i in range(100):
#     liss.append(print(i))

# print(liss)
# print(len(set(lst)))   # None

# a = [2, 1, 2, 4]
# a[1:].remove(2)
# print(sum(a))            # 9

# a = [1, 2, 3, 4]



# class h:
#     def f(self, n):
#         print(name)
#         print(n)

# name = h()
# print(name.f('dead'))
# print(name)


a = [1, 2**2]
b = [1, 2*2]

x = 2*2
y = 8/2
print(a == b)
print(x == y)
if (x is y) | (a is b):
    print(1)
else:
    print(0)
