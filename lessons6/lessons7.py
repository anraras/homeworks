# -*- coding: utf-8 -*-


def switch(enabled=True):
    def decor(func):
        def wrapper(*args, **kwargs):
            if enabled is True:
                print('Function {} enabled'.format(func.__name__))
                return func(*args, **kwargs)
            else:
                print('Function {} disabled'.format(func.__name__))
                return None
        return wrapper
    return decor


@switch()
def some_logic(x, y):
    return x + y


print(some_logic(2, 3))
