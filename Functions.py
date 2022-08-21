# Demonstrate the capabilities of functions

# Two different types of function arguments - positional (required, ordered in positions), keyword (order not important,
# assigned a default value. Keyword argument must be last everywhere
def foo(a, b, c=0):
    print(a, b, c)


print("Positional/Keyword arguments:")

foo(1, 2)  # Only use positional arguments - note that the default is printed

foo(1, 2, c=3)  # Use the keyword argument as well
foo(1, 2, 3)  # Does the same thing as the line before

# *args and **kwargs

print("\nArguments:")


# One star means you can pass any number of arguments you want to the function, two stars mean you can pass any keyword
# args is a tuple, kwargs is a dict
def var_arguments(a, b, *args, **kwargs):
    # Print the mandatory args
    print(a, b)

    # Print additional regular arguments
    for arg in args:
        print(arg)

    # Print keyword argument keys and values
    for key in kwargs:
        print(key, "-", kwargs[key])


var_arguments(1, 2, 4, 5, test=True, h=3)

# Mandatory keywords

print("\nMandatory keywords:")


# Everything after the star is a mandatory keyword
def mandatory_keyword_args(a, b, *, c, d):  # *args also works instead of * if you want variable arguments as well
    print(a, b, c, d)


mandatory_keyword_args(1, 2, c=3, d=4)

# Unpack arguments from an iterable

print("\nUnpack args/kwargs:")


def unpack_args(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
unpack_args(*my_list)  # Star is not a pointer, it unpacks the arguments in the iterable - lengths must match

# Unpack kwargs

my_dict = {'a': 1, 'b': 2, 'c': 3}
unpack_args(**my_dict)  # Use two stars to unpack kwargs from a dictionary

# Global

print("Global example:")


def global_test():
    global num
    num = 3


number = 0  # Can be defined after the func!
global_test()
print(number)
