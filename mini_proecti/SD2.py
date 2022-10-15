
                                                        # calculator

while True:
    print('')
    print('for breakking program ente (stop)')
    print('')
    sign = input('+ - * /\nenter sign: ')
    if sign == 'stop':
        break

    n1 = None
    n2 = None
    
    if sign in ('+','-','*','/'):

        while True:    
            n1 = input('enter number_1: ')
            try:
                n1 = float(n1)
                break
            except ValueError:
                print('enter correct number')
                continue                  
        
        while True:
            n2 = input('enter number_2: ')
            try:
                n2 = float(n2)
                break
            except ValueError:
                print('enter correct number')
                continue

    else:
        print('enter correct value!')
        continue

    if sign == '+':
        print('your answer',n1 + n2)
    elif sign == '-':
        if n1 - n2 < 0:
            print('your answer lower than zero..!',n1 - n2)
        else:
            print('your answer',n1 - n2)
    elif sign == '*':
        print('your answer',n1 * n2)
    elif sign == '/':
        if n1 == 0 or n2 == 0:
            print('devision by zero...!')
        else:
            print('your answer',n1 / n2)

print('we hope you will back :)')