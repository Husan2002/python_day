def upgrate_to_dict(**kwargs):
    for i in kwargs:    
        print(i,kwargs[i])

upgrate_to_dict(name = input('enter name: ').capitalize(), surname = input('surname: ').capitalize(), age = int(input('enter age: ')), country = input('enter country: ').capitalize(), password = input('enter password: '))

