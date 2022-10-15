"""
welcome
watch
add
remove
quit

"""
spisok = []

class ToDo():
    global rule_1
    global spisok
    global remove
    
    def popolnenie():
        global spisok
        spisok = []
        while 1:
            print('\nfor breaking program enter (done)\n')
            todo = input('please edd actions for todo: ')
            if todo == 'done':
                break
            spisok.append(todo)
            print(spisok)

    # popolnenie()


    def prosmotr():
        for i in spisok:
            print(i)


    # prosmotr()


    def udalenie():
        global remove
        while 1:    
            remove = input(f'{spisok}\nplease remove actions from list: ')
            if remove == 'done':
                break
            spisok.remove(remove)
            

    # udalenie()

    def pravila():
        global rule_1
        rule_1 = 'Todo\n  This is big list where your write actions\n  and after (done) actions you can delete them.\n  You can also watch your actions from yor Todo list.\n  This program will help you remember\n  what you have to do today\n  Let\'s go.!'

        print(rule_1)

    # pravila()


