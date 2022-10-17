# a = 2
# b = 5

# if a > b:
#     print(a)
# else:
#     print(b)


a = 3
b = 5

# print(a if a > b else b)



# ternarniy operator

# max = a if a > b else b
# print(max)

# is_fast = True
# if is_fast:
#     car = 'ferrari'
# else:
#     car = 'tico'
# print(car)


car = "ferrari"

speed = 'ferrari' if True else 'tico'
# print(speed)



# car = 'ferrari' if car == 'ferrari' else 'tico'
# print(car)

'''
ili

'''
# car = 'far' if True else 'tico'

a,b,c = 13, 66, 32

max = a if a > b and a > c else b if b > c else c
# print(max)

# max = a if a > b and a > c else b if b > c else c


a1 = [i for i in range(1, 100)]
# print(a1)


for i in range(10):
    i **= i
# print(i) 

x = [i**2 for i in range(1, 10)]
# print(x)



x1 = [i for i in range(1, 20) if i %2 == 0]
# print(x1)


x2 = [i for i in range(1, 20) if i %2 != 0]
# print(x2)


x3 = [i*2 for i in 'python']
# print(x3)

def sum_two(a, b):
    print(a*b)

# sum_two(4, 6)


x4 = lambda a, b: a * b 
# print(x4(4,6))
# print((lambda a, b: a * b)(4, 6))


# print((lambda a, b: a * b)((float(input('enter number: '))),(float(input('enter number: ')))))

# lambda arguments: ispolneniye ili operatsiya



# step = [i**i for i in range(10)]
# print(step)


# step1 = [i for i in range(100) if i % 2 == 0]
# step2 = [i for i in range(100) if i % 2 != 0]
# print(step1)
# print(step2)


# a4 = [i * 2 for i in 'python']
# print(a4)


# pustoy = []

my_pets = ['mgid','gthfg','ethtyjghj','ehtjtuj']


# print(str(my_pets).upper())
# print(type(str(my_pets).upper()))


upper_text = []

for i in my_pets:
    i2 = i.upper()
    upper_text.append(i2)
# print(upper_text)
# print(type(upper_text))

x6 = list(map(str.upper, my_pets))
# print(x6)
# print(type(x6))





# # my_pets = str(my_pets).upper()
# # print(my_pets)

# print(list(map(str.upper, my_pets)))


# print(list(map(len, my_pets)))

nums = [3.356734, 5.65334, 7.2312, 64.623234, 128.214]

# print(round(4.45112))
# print(round(4.50000))
# print(round(4.513423))

# print(list(map(round,nums ,range(1, len(nums)))))
# print(list(map(round, nums, range(1, len(nums)))))

my_pets1 = ['mgid','gthfg','ethtyjghj','ehtjtuj']
# print(list(map(lambda i: i*2, my_pets1)))

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda x: x > 70, scores)))

mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']  
# print(list(filter(lambda z: z == 'мак', mixed)))

dromes = ("анна", "жанна", "rewire", "madam", "freer", "anutuna", "kiosk")
# print(list(filter(lambda a1: a1 == a1[::-1], dromes)))

# # Пример №4 / четные числа
numbers = [2, 1, 3, 4, 7, 11, 18]
# print(list(filter(lambda nechot: nechot %2!=0, numbers)))
# print(list(filter(lambda chot: chot %2==0, numbers)))



# sum_f = lambda a, b: a*b
# print(sum_f(54,23))

# # Ниже приведен список баллов 10 студентов на экзамене по химии. Давайте отфильтруем тех, кто сдал с баллом выше 75. используя filter.
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

# print(list(filter(lambda i: i > 75, scores)))

# # Пример №2 / мы ищем в городе заведения с названием мак и мы должны их отфильтровать, чтобы выходило только "мак"
# mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']

# print(list(filter(lambda a: a == 'мак', mixed)))

# # Пример №3 / Следующим примером будет детектор палиндрома. «Палиндром» - это слово, фраза или последовательность, которые читаются одинаково в обе стороны. Давайте отфильтруем слова, являющиеся палиндромами, из набора (iterable) oподозреваемых палиндромов.
# dromes = ("анна", "жанна", "rewire", "madam", "freer", "anutuna", "kiosk")

# print(list(filter(lambda a: a[0::] == a[::-1], dromes)))

# # Пример №4 / четные числа
# numbers = [2, 1, 3, 4, 7, 11, 18]
# print(list(filter(lambda i: i% 2 != 0, numbers)))

# maxito