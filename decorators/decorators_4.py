# Applying Multiple Decorators to a Single Function

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
@split_string
def say_my_name():
    return 'Daniel the beast'

print(say_my_name())