import random

kount = 0
def main():
    while 1:
        
        global kount
        random_number = random.randint(1,8)
        user_input = int(input('enter number: '))
        kount += 1
        if kount > 5:
            print('you lose')
            break

        if user_input == random_number:
            print('you win')
            break
        elif user_input > random_number:
            print('take lower')
        elif user_input < random_number:
            print('take higher')
        
            
main()
