from contextlib import contextmanager

# Context managers manage opening and closing resources automatically

# Open and close a file appropriately with or without an exception
with open('notes.txt', 'w') as file:
    file.write('Hello')


# Locks as used in Threading&Processing also used with context managers

# Create your own context manager from a class

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
        print('init')

    # Whenever you enter the context manager
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    # Whenever you exit the context manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print('exit')


with ManagedFile('notes.txt') as file:
    file.write('Do some stuff.')


# Implement context managers as a function

@contextmanager
def open_managed_file(filename):
    # __enter__ function
    f = open(filename, 'w')

    try:
        yield f
    finally:
        # __exit__ function
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('Do some more stuff')
