def decorator(func):
    def wrapper(*args, **kwargs):
        print('before func')
        print(func(*args, **kwargs))
        print('after func')
    return wrapper


@decorator
def plus(x: int):
    return x**2


plus(5)