# def new_order():
#     answer = input =('order \ny/n')
#     if answer == 'y':
#         return True
#     elif answer == 'n':
#         exit()

# def get_order(order):
#     order = []
#     for ing in ingridients:
#         command = input(f'add: {ing}; y/n')
#         if command == 'y':
#             order.append(ing)
#         return order

# def 

# def main():
#     ingridients = ['maenez','ketchup','ananas','sir','kalbasa','trabka','zelen']
#     new_order()

# main()


# Задача №1 - нужно объединить два списка, а повторяющиеся элементы выкинуть


list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']

# list_names.extend(get_names)
# print(set(list_names))

# print(list(set(list_names+get_names)))


# Задача №2 - в строке нужно найти все числа и составить их в список "frg5gth57ubdfh9sbf4dsbdr0dxbf2"
my_str = "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2"

num_list = []
for i in my_str:
    try:
        int(i)
    except ValueError:
        pass
    else:
        num_list.append(int(i))


print(num_list)

