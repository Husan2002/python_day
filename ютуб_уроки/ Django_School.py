# game = input('play..?: ')

# while game == 'ok':
#     num = '15'
#     guess = input('guess numner: ')

#     if guess == num:
#         print('you win')
#     else:
#         print('you louse')
    
#     ques = input('play again?: ')

#     if ques == 'no':
#         break
#     else:
#         continue


password_list = ['password', '12 3456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567']
name = input('enter name please: ').capitalize()
print('')
countn = 0

while 1:
    pin = input(f'enter password: ')
    if pin not in password_list:
        countn += 1
        if countn > 2:
            print(f'sory {name}\nbut you miss your chanse bye')
            break
        print('incorrect..!')
        continue
    else:
        print('correct')
        print(f'welcome to our program developer {name}')
        break
