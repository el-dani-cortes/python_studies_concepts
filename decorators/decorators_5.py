# Defining General Purpose Decorators

# General decorator
def decorator_passing_arbitrary_arguments(function_to_decorate):
    def wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return wrapper_accepting_arbitrary_arguments

# No arguments -----------------------
@decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

print("\nNo arguments -----------------------")
function_with_no_argument()

# Positional arguments -----------------------
@decorator_passing_arbitrary_arguments
def function_with_arguments():
    print(a, b, c)

print("\nPositional arguments -----------------------")
function_with_arguments(1,2,3)


# Keyword arguments -----------------------
@decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

print("\nKeyword arguments -----------------------")
function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")
