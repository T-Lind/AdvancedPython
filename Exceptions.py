# Errors and exceptions
# Exception = error during runtime

# Force an exception
x = 5

if x < 0:
    raise Exception('x should be positive!')  # like throw new in Java

assert (x >= 0), 'x is not positive'  # if the first statement is false then throw an AssertionError with the statement

# try/except statement
try:
    # a = 5 / 0  # causes a ZeroDivisionError
    b = 5 + '10'
except TypeError as e:  # best practice to use specific error, not broad Exception
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:  # catches all exceptions
    print(e)
else:  # Executes if everything ran without errors
    print("Everything is good!")
finally:  # Always executes no matter if there was an error or not
    print('cleaning up')


# Do this in a separete file generally (here for continuity)
class ValueTooHighError(Exception):  # This is python inheritance by the way
    pass  # By passing it just creates an empty class with inheriting whatever Exception has


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message  # assigning member data
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 0:
        raise ValueTooSmallError('value is too small', x)  # Remember, python only allows ONE constructor


try:
    test_value(-1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
