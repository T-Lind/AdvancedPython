import functools


# Decorators - function and class decorators

# Function decorators allow you to add functionality to a function without overriding current functionality

# Important - python functions are actually CLASS objects! aka you can have a function in a function,
# passed as an argument, returned from functions

def start_end_decorator(func):
    def wrapper():
        print("Start")  # DO SOMETHING BEFORE THE FUNCTION
        func()
        print("End")  # DO SOMETHING AFTER THE FUNCTION

    return wrapper  # DECORATOR MUST RETURN A FUNCTION!


@start_end_decorator
def print_name():
    print('Alex')


# Simply print 'Alex'
print("No decorator:")
print_name()

# Use decorator functionality - redefine function
# print_name = start_end_decorator(print_name)  # Does the same thing as @start_end_decorator


print("With decorator:")
print_name()


# add5 with decorator

def start_end_decorator(func):
    @functools.wraps(func)  # Reserve info of used function
    def wrapper(*args, **kwargs):  # Use as many arguments as you want
        print("\nStart")  # DO SOMETHING BEFORE THE FUNCTION
        result = func(*args, **kwargs)
        print("End")  # DO SOMETHING AFTER THE FUNCTION
        return result

    return wrapper  # DECORATOR MUST RETURN A FUNCTION!


@start_end_decorator
def add5(x):
    return x + 5


print(add5.__name__, add5(5),"\n")


# Use a decorator to repeat a function's execution a number of times and give information
# about a function with a decorator

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper


@debug
@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')
    return name

greet("Bob")


# Class decorators - maintain and update a state

class CountCalls:  # Documentation example below using multi line strings
    """
    A class decorator to count the number of calls a function has been run through.
    """
    def __init__(self, func):
        """
        Init function to assign a function (called indirectly with a decorator)
        :param func: The input function
        """
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        """
        The function to execute when the class is called
        :param args: Arguments of the input function
        :param kwargs: Keyword arguments of the input function
        :return: The function which has run
        """
        self.num_calls += 1
        print(f'This function has executed {self.num_calls} time(s).')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


say_hello()  # Will print it has executed 1 time
say_hello()  # Will print it has executed 2 times
