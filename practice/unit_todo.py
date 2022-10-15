from todo import todo, Todo


create_todo = input('Создать туду? \n Да Нет\n')

if create_todo == 'Да':
    name = input('What is your name? :')
    pincode = input('create pincode: ')
    rules = []
    
    while True:
        print('If yopu want to exit enter "done" \n or')
        rule = input('Enter some rule: ')
        if rule == 'done':
            break
        else:
            rules.append(rule)
            continue
    some_todo = Todo(pincode=pincode, name=name, rules=rules)

    methods = [method for method in dir(some_todo) if method.startswith('__') is False]
    
    enum_methods = enumerate(methods, 1)
    print(list(enum_methods))
    for i in list(enum_methods):
        print(f"{i[0]}:{i[1]}")
    print('Enter method by number!')

    number = int(input('Select: '))


    
else:
    print('ok :(')
