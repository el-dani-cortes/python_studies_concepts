# Decorators that can take arguments themselves
from functools import wraps


def meta_decorator(power):
    def decorator_list(fnc):
        @wraps(fnc)
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    return decorator_list


@meta_decorator(2)
def add_together(a, b):
    """ hola add"""
    return a + b

print(add_together.__doc__)
print(add_together.__name__)

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))