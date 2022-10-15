# # # problem:1
# # name = input('enter name: ').title()
# # print(f'Hello my friend {name} '*5)

# # problem:2
# name1 = input ('Как вас зовут?: ')
# age = float(input ('Сколько вам лет?: '))
# geo = input ('Где вы учитесь/работаете?: ')
# line = input ('Какая сфера IT вас интересует?: ')
# language = input ('На каком языке вы программируете?: ')
# print('')
# print(f'Data of student {name1.title()}')
# print('')
# print(f'name of student: {name1.title()}')
# print(f'age of student: {age}')
# print(f'location by study: {geo}')
# print(f'type of line IT: {line}')
# print(f'program language: {language}')

# # problem: 3
# stroka = input('enter any word: ')
# word_length = len(stroka)
# print(f"{stroka} " * word_length)


# problem: 4
def palindrom():
    stroka1 = input('enter name for knowing polindrom: ')
    if stroka1 == stroka1[::-1]:
        print('palindrom')
    else:
        print(False)

palindrom()

# problem: 5
word = 'text of this language'
print(word[0],word[-1])

# problem: 6
our_numbers = '123456789'
print(our_numbers [0:10:2])
print(our_numbers [1:10:2])
