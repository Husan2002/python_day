# numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers.append(20)
# print(numbers)

# numbers.reverse()
# print(numbers)

# numbers.extend(['something',['wsfdgh']])
# print(numbers)


# numbers.insert(4, 43)
# print(numbers)

# x = [i for i in range(1, 11)]
# print(x)

# ''''''
# x = [i for i in range(1, 11, 2)]
# print(x)


# # ==

# n = []
# for i in range(1, 11, 2):
#     n.append(i)
# print(n)

# ''''''


# list1 = [11, 33]
# list2 = [1, 9]
# list3 = list1 + list2
# print(list3)

# list4 = [1, 2, 3, 4]
# list5 = list4 * 3
# print(list5)

# list1 = [11, 22, 44, 16, 77, 98]
# print(22 in list1)

# print(22 not in list1)

# '''
# list_1 = [1,2,3,4,5]
# for i in list_1:
#     print(i, end=',')
# ?
# ''' 
# # correct
# my_list = ['hasan', 'husan', 'aziz']
# print(','.join(my_list))
# print('\n'.join(my_list))


# list_of_ints = [80, 443, 8080, 8081]
# print(str(list_of_ints).strip('[]'))
# # ili
# print(str(list_of_ints)[1 : -1])
# # udalyaet pervuyu skobku i polsednuyu sjobku

# print(' '.join(map(str, list_of_ints)))
# print('\n'.join(map(str, list_of_ints)))


# print([1,2]*3)

# a = [ 1, 342, 223, 'Африка', 'Очки']
# print(a[-3])

# sample = [10, 20, 30]
# sample.append(60)
# sample.insert(3, 40)
# print(sample)

# lake = ["Python", 51, False, "22"]
# lake.reverse()
# lake.reverse()
# print(lake[-2])

# x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']

# for i in x[1]:
#     # print(i)
#     if type(i)==list:
#         for el in i:
#             if el == 'baz':
#                 print(el)

# s = input()
# print(s.split())

# s1 = input(': ').split()
# print(s1)

# a = (list(map(int, input(': ').split())))
# print(a)

# b = (dict(map(int, input().split())))
# print(b)


# # vvod otretsatelnix na polojitelnie7

# c = int(input('enter: '))
# if c < 0:
#     print(f'perevoe: {c} vtoroe {abs(c)}')




# names = ['tolik','bobik','sharik']


# for name in names:
#     print(name)

# names.append('simba')
# print(names)

# names.pop()
# print(names)

# n = names.index('bobik')
# print(n)

# sort_1 = [21, 43, 786, 12, 88, 3, 12, 877, 12, 982]
# sort_1.sort(reverse=True)
# print(sort_1)

# sort_2 = [21, 43, 786, 12, 88, 3, 12, 877, 12, 982]
# sort_2[4] = 'b'
# print(sort_2)

# sort_3 = ['dsfsad','sdfs','1qwd','afdsd']
# sort_3.sort()
# print(sort_3)


# sort_4 = [2.1, 4.3, 78.6, 1.2, 8.8, 3.0, 12, 87.7, 12, 98.2]
# sort_4.sort()
# print(sort_4)