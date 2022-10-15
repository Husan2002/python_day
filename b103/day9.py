def b103():
    print('heelo')

b103()

''''''

def b104(message):
    print(f'hi {message}')

b104('husan')

''''''

def sum2(a,b):
    print(a * b)

sum2(12,44)

''''''

def isPositive(x):
    if x > 0:
        return True

p = []
for i in range(-12, 13):
    if isPositive(i):
        p.append(i)

print(p)

''''''


total = 0

while True:
    def calc():
        global total
        operation = input("+, - , *, /\nОчистить историю\n")
        if operation == 'Очистить историю':
            total = 0
        elif total != 0:
            num1 = input("введите число: ")
            try:
                float(num1)
            except ValueError:
                print('Введите только числа')
            else:
                try:
                    num1 = float(num1)
                    if operation == '+':
                        total += num1
                        print(total)
                    elif operation == '-':
                        total -= num1
                        print(total)
                    elif operation == '*':
                        total *= num1
                        print(total)
                    elif operation == '/':
                        total /= num1
                        print(total)
                    else:
                        print("ошибка")
                except ZeroDivisionError:
                    print('На нуль делить нельзя!')

        elif operation in ('+', '-' , '*', '/') and total == 0:
            num1 = input("введите число: ")
            num2 = input("введите число: ")
            try:
                float(num1)
                float(num2)
            except ValueError:
                print('Введите только числа')
            else:
                try:
                    num1 = float(num1)
                    num2 = float(num2)
                    if operation == '+':
                        total += num1 + num2
                        print(total)
                    elif operation == '-':
                        total += num1 - num2
                        print(total)
                    elif operation == '*':
                        total += num1 * num2
                    elif operation == '/':
                        total += num1 / num2
                    else:
                        print("ошибка")
                except ZeroDivisionError:
                    print('На нуль делить нельзя!')
            finally:
                print("___________________________")
        else:
            print("тебя же просят ввести символ! совсем!")

    calc()   