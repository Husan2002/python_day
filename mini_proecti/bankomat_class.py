pincode_in_db = '1234'

class Bankomat:
    def __init__(self, pincode: str, balance: str, name: str):
        self.pincode = pincode
        self.balance = balance
        self.name = name
        print(f'Welcome to Husan\'s bankonat {name}')

    
    def check_pinkode(self):
        if self.pincode == pincode_in_db:
            return True
        else:
            return False


    def pay(self, amount):
        if self.check_pinkode():
            self.balance += amount
            return f'Pay Done!({amount})\n{self.get_balance()}'
        else:
            return "Incorrect pincode"


    def withdraw(self, amount):
        if self.check_pinkode():
            if self.balance > amount:
                self.balance -= amount
                return f'Withdraw Done({amount})\n{self.get_balance()}'
            else:
                return 'Not enough money!'
        else:
            return 'Inccorrect pincode'


    def get_balance(self):
        if self.check_pinkode():
            return f"your banance is {self.balance}"
        else:
            return 'Inccorrect pincode'

user_pinkode = input('enter pincode: ')
name = input('Enter your name: ')
User = Bankomat(pincode=user_pinkode, balance=0, name=name)

while True:
    print('IPOTEKA BANK\nviberite odin iz etix variantov.')
    print('\nposmotret balans-1    popolnit balans-3\n    snyat dengi-4')
    command = input("command: ")
    if command not in ('1','2','3','4'):
        print('                        please chose one of these nubers (1,2,3,4)...!')
        continue

    if command == "1":
        print(User.get_balance())
    elif command == "3":
        print(User.pay())
    elif command == '4':
        print(User.withdraw())