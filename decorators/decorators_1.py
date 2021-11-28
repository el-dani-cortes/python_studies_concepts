# # Example of decorators
from functools import wraps

# # Case #1 ---------------------
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = my_decorator(say_whee)


# Case #2 ---------------------
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_yupi():
    """ Soy yupi elegante"""
    print("Yupi!!!")

print(say_yupi.__name__)
print(say_yupi.__doc__)

if __name__ == "__main__":
    # print("----- Case 1 -----")
    # say_whee()
    print("\n----- Case 2 -----")
    say_yupi()