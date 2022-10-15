
# def add_meal():
#     while 1:
#         print('\nif tou done enter (0)')
#         add_bluda = int(input('add_viberite po nomeru: '))-1
#         if add_bluda == -1:
#             break
#         lst.append(add_bluda)
#         print(lst)

# add_meal()


# def delete_meal():
#     while 1:
#         print('\nif tou finish enter (0)')
#         del_bluda = int(input('delete_viberite po nomeru: '))-1
#         if del_bluda == -1:
#             break
#         lst.pop(del_bluda)
#         print(lst)

# delete_meal()


# def show_choice():
#     num_c = 0   
#     for i in lst:   
#         num_c += 1  
#         print(f'{num_c}.{i}')

# show_choice()

lst = []

while 1:
    print('if you finish enter (done)')
    add_bluda = input('choice the number and add food:')
    if add_bluda == 'done':
        print(lst)
        break
    lst.append(add_bluda)                               # naado rabotat
    print(lst)





while 1:
    print('if your choice correct enter (done) if not remove')
    rem_bluda= input('choice the number and remove food:')
    if rem_bluda == 'done':
        print(lst)
        break
    lst.pop(rem_bluda)                             
    print(lst)

