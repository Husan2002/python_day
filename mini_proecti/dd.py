while True:
    print('')
    print('for breaking program enter (stop)')
    s = input('+ - * /\nenter sign: ')
    if s == 'stop':
        break
    elif s not in ('+','-','*','/'):
        print('enter correct sign..!')
        continue
    a = float(input('enter number: '))
    b = float(input('enter number: '))

    if s == '+':
        print(a + b)
    elif s == '-':
        if a - b < 0:
            print('your answer lower than zero..!',a - b)
        else:
            print(a - b)
    elif s == '*':
        print(a * b)
    elif s == '/':
        if a == 0 or b == 0:
            print('division by zero',a / b)
        else:
            print(a / b)


print('we hope you will back..!')