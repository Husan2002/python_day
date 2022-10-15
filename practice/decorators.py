def check_pincode(func):
    def wrapper(*args, **kwargs):
        try:
            self = args[0]
            if self.authenticated:
                print(func(*args, **kwargs))
            else:
                raise "Sorry, your pincode is incorrect"
        except AttributeError:
            print('This is the function(must be method of class)')
    return wrapper


# @check_pincode
# def sad(*args):
#     lst = []
#     for i in args:
#         lst.append(i)
#     return lst


# sad(1,2,4,'32423',42)