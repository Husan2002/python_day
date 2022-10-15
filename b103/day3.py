if 13 > 4:
    print('word')
elif 33 > 5:
    print('aga 2')
else:
    print('fig tibe')


person = float(input('your age: '))
if person >=0 and person < 18:
    print('eho malish! ')
elif person >= 18 and person < 40:
    print('idyom gulyat')
elif person >= 40 and person < 70:
    print('ctariy uje!')
elif person >= 70 and person <= 140:
    print('ne tuda popali')
else:
    print('oshibka!')



num1 = int(input('enter num: '))
l = []
l1 = []
if num1 % 2 == 0:
    l.append(num1)
    print('chotnie:',l)

elif num1 % 2 != 0:
    l1.append(num1)
    print('ne chotnie:',l1)



a = [12, '2edsfs', True, {'danit'}]
a[1] = 'endzen'
a[-1] = 'nuna'
a.append(False)
b = [123,64543,45,876,]
a.append(b)


print(a)

third_elem = 'pod tri'

my_list = ['один', 'два', 'три', 'четыре', 'пять']
print(my_list)

my_list[2] = third_elem 
print(my_list)

my_list_1 = ['один', 10, 2.25, [5, 15], 'пять']
print(my_list_1)

my_list[-1]  =  'ноль'
print(my_list)

'''
Если индекс — отрицательное число, то он будет считаться с последнего элемента.
'''

elem  =  my_list[-1]
print(elem)



'''
on dobovlyaet posle pervovo indexa
'''

my_numbers = [1, 2, 3, 4, 5]
my_numbers.insert(1,'Привет')
print(my_numbers)