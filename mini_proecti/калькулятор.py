while True:
    print('')
    print('for breakking program ente (done)')
    print('')
    sign = input('+ - * /\nenter sign: ')
    if sign == 'done':
        break
    a = None
    b = None
    
    if sign in ('+','-','*','/'):
        while True:    
            a = input('enter number1: ')
            try:
                a = float(a)
                break
            except ValueError:
                print('enter correct number')
                continue   

        while True:
            b = input('enter number2: ')
            try:
                b = float(b)
                break
            except ValueError:
                print('enter correct number')
                continue
    else:
        print('enter correct value!')
        continue
    if sign == '+':
        print('your answer',a + b)
    elif sign == '-':
        if a - b < 0:
            print('your answer lower than zero..!',a - b)
        else:
            print('your answer',a - b)
    elif sign == '*':
        print('your answer',a * b)
    elif sign == '/':
        if a == 0 or b == 0:
            print('devision by zero...!')
        else:
            print('your answer',a / b)
print('we hope you will back :)')



