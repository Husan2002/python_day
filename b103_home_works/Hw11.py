# def new_roder():
#     answer = input('budite delat zakaz? \ny/n: ')
#     if answer == 'y':
#         return True
#     elif answer == 'n':
#         exit()

# def get_otder(ingridients):
#     order = []
#     for ing in ingridients:
#         command = input(f'dobavit ingredient: {ing}: y/n')
#         if command == 'y':
#             order.append(ing)
#     return order

# def check_order(order):
#     if not order:
#         print('vi nichevo ne zakazali..!')
#         new_roder()
#     for ing in order:
#         print(ing, end =', ')
#     res = input('verniy li vash zakaz?\n y/n: ')
#     if res == 'y':
#         print('zakaz prinet! podojdite')
#         return True
#     elif res == 'n':
#         new_roder()
        

# def main():
#     ingridients = ['ketchup', 'maynez', 'tamat', 'ananas', 'perets', 'kalbasa', 'travka']
#     new_roder()
#     order = get_order(ingridients)
#     if check_order(order):
#         exit() 
        
# main()




def new_order():
    answer = input('wana order?:\ny/n\n: ')
    if answer == 'y':
        return True
    elif answer == 'n':
        exit()


def get_order(ingredients):
    order = []
    for ing in ingredients:
        command = input('add ingridient {ing}?:\ny/n: ')
        if command == 'y':
            order.append(ing)
    return order

def check_order(order):
    if not order:
        print('vi nichevo ne dobavili!')
        new_order()
    for ing in order:
        print(ing, end=', ')
    res = input('verniy li vash zakaz?\ny/n\n')
    if res == 'y':
        print('zakaz prinet! Podojdite')
        return True
    elif res == 'n':
        new_order()

def main():
    ingridients = ['ketchup', 'maynez', 'tamat', 'ananas', 'perets', 'kalbasa', 'travka']
    new_order()
    order = get_order()
    if check_order(order):
        exit()

main()
