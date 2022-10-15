def mini_kalkulator():
    while 1:
        print('')
        print('welcom to our calculator')
        s = input('enter sign: ')
        if s == 'stop':
            print('we hope you will back :)')
            break
        elif s not in ('+','-','*','/'):
            print('enter corect sign please..!')
            continue
        n1 = float(input('1_enter number: '))
        n2 = float(input('2_enter number: '))

        if s == '+':
            print('your result:',n1 + n2)
        elif s == '-':
            if n1 - n2 < 0:
                print('your answer lower than zero:',n1 - n2)
            else:
                print('our result:',n1 - n2)
        elif s == '*':
            print('our result:',n1 * n2)
        elif s == '/':
            if n1 == 0 or n2 == 0:
                print('division by zero..!',n1 / n2)
            else:
                print('our result:',n1 / n2)
