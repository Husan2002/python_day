balans = 435
password = '2002'
while 1:
    print(balans)
    print('')
    print('for breakking program enter (stop)')
    print('')

    print('IPOTEKA BANK\nviberite odin iz etix variantov.')
    print('\nposmotret balans-1    kredit-2\npopolnit balans-3    snyat dengi-4')
    menu_1 = (input(':'))
    if menu_1 == 'stop':
        print('IPOTEKA BANK mi budem jdat vas :) ..!')
        break
    elif menu_1 not in ('1','2','3','4'):
        print('                        please chose one of these nubers (1,2,3,4)...!')
        continue

    if menu_1 == '1':
        while 1:
            password = input('please enter pincode: ')
            if password == '2002':
                print('your balans has',balans,'som')
                break
            else:
                print('                                 please enter correct pincode...!')
                continue
    elif menu_1 == '2':
        while 1:
            password = input('please enter pincode: ')
            if password == '2002':
                print('skolka vi xotite vzat v kredit:')
                kredit = int(input(':'))
                print('vash balans:',balans,'\nvi vzali ',kredit,'somov\nvash balans popolnen na',kredit + balans)
                break
            else:
                print('                                 please enter correct pincode...!')
                continue
    elif menu_1 == '3':
        while 1:
            password = input('please enter pincode: ')
            if password == '2002':
                popolnenie = int(input('skolka vi xotite dobavit: '))
                balans += popolnenie
                print('vash balans:',balans,'\nvi vveli ',popolnenie,'som\nvi uspeshno vveli kapital obshaya somma sostovlaye',popolnenie + balans)
                break
            else:
                print('                                 please enter correct pincode...!')
                continue
    elif menu_1 == '4':
        while 1:
            password = input('please enter pincode: ')
            if password == '2002':
                snyat = int(input('skolka vi xotite snyat: '))
                print('vash balans ',balans,'\nvi snyali',snyat,'som\nvi uspeshno snyali dengi iz kapitala',balans - snyat)
                break
            else:
                print('                                 please enter correct pincode...!')
                continue