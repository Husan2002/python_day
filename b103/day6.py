

# int - 1, 2, 3, 4,....
# str - 'text'
# float - 1.0, 2.0, 3.0, 4.0,....
# bool - True, False

'''

tuple - ()
list - []
dict - {}
set - {}

'''

# Создание словаря c помощью литерала

# student = {'name':'Ivan', 'age':12}
# credentials = {'email':'hacker1337@mail.ru', 'password':'123456'}

# Создание словаря c помощью функции dict()

student = dict(name='Ivan', age=12)
credentials = dict(email='hacker1337@mail.ru', password='123456')


# menyat
student['name'] = 'Vasya'
print(student['name'])

# udalit
del student['age']
print(student)


# print(value)
print(student.get('lastname', 'No key'))







# 44 minuta dz