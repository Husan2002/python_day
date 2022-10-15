program_name = 'Rider'
program_age = 7

print('Vas privestvuet',program_name)
name = input('kak vas zovut: ').title()
print(f'Privet {name}\nnapeshite familiyu')
surname = input(':').title()
print(f'Okey {name} {surname} ya zapomnyu vas\nteper veditr svoy vozrost')
age = float(input(':'))

if age <= 11:
    print('Ogo',name,'vi starshe menya na',age-program_age,'goda mne',program_age)
elif age > 11:
    print('Ogo',name,'vi starshe menya na',age-program_age,'let mne',program_age)

print(age - program_age,'let nazat vam bilobi',program_age,'kak i mne i mi igralibi v meste :)')

dog = input('u vas est sobaka?\nda ili net: ')

if dog == 'da':
    dog_name = input('kak ee zovut: ')
    print('skolka',dog_name+'u','let')
    dog_age = float(input(':'))
    print('xmm da on mladshe vas na',age - dog_age,'let\nklassno ya shitayu imet sobaku eto xorosho!')
    print('')
elif dog == 'net':
    print('')
    print('xmm u menya toje netu')
    print('ladno davayte zaymemsya chem nibut koneshno esli vi ne ustali')

print('nu',name,'esho ne ustali?')
vremenniy_vopros = input(':')
if vremenniy_vopros == 'net':

    razresheniya_poigrat = input('togda davay poigraem v kalkulyatori\nda ili net: ')
    
    if razresheniya_poigrat == 'da':
        print('prekrasno')
        
        while True:
            print('')
            print('for breakking program enter(stop)!')
            sign = input('+ - * /\nenter sign: ')
            if sign == 'stop':
                print('....')
                print('We hope you will back\nBye :)')
                break
            if sign not in ('+','-','*','/'):
                continue
            num1 = float(input('enter number: '))
            num2 = float(input('enter number: '))
            if sign == '+':
                print('your answer',num1 + num2)
            elif sign == '-':
                if num1 - num2 < 0:
                    print('your answer lower than zero',num1 - num2)
                else:
                    print(num1 / num2)
            elif sign == '*':
                print('your answer',num1 * num2)
            elif sign == '/':
                if num1 == 0 or num2 == 0:
                    print('division by zero..!!!')
                else:
                    print('your answer',num1 / num2)

    
    elif razresheniya_poigrat == 'net':
        print('')
        print('znachit vi ustali',name,'lol')

elif vremenniy_vopros == 'da':
    print('Togda mi s vami proshaemsya')    
    
print('Kak vi znayte menya zovut',program_name,'\nNe zabut eta imya mi esho ne raz budem vstrechatsya s vami :)')

