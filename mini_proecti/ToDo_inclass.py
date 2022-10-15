todo = ['закончить первый класс', "почистить зубы", "принять душ с шампунем"]
while True:
    destvie = input("Выберите действие:\n1 - это добавление\n2 - это удаление\n3 - это просмотр\n4 - выйти из программы\n")
    if destvie == '3':
        for i in todo:
            print(i)
    elif destvie == '1':
        delo = input("добавляй дело: ")
        todo.append(delo)
        print(f"успешно добавлено: {delo}")
    elif destvie == '2':
        # remove - удаление по значению
        # del_delo = input("удалить дело: ")
        # if del_delo in todo:
        #     todo.remove(del_delo)
        # print(todo)    
        # remove - удаление по значению
        # по индексу
        del_delo = int(input("удалить дело: \nУдаление происходит по индексу(индексы начинаются с нуля): "))
        todo.pop(del_delo)
        print(todo)
    elif destvie == '4':
        ty_ne_tupoi = input("уверены что хотите выйти\nyes / no: ")
        if ty_ne_tupoi == 'yes':
            # exit()
            break
        elif ty_ne_tupoi =='no':
            continue


