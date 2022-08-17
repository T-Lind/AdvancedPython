import sys
import timeit

# Tuples are immutable

# Create a tuple
mytuple = ("Max", 28, "Boston")  # Parenthesis are optional for tuples
print("Tuple:", mytuple)

# Create a tuple with one element - the comma is necessary, otherwise it will be considered a string
a_tuple = ("Max",)

# Use the tuple function to convert from a list to a tuple
a_list = [1, 5, 7, 9, 112]
tuple_from_list = tuple(a_list)
print(tuple_from_list)

# Get an item through an index - same as lists
print("First element in the tuple:", mytuple[0])

# mytuple[0] = "Tim" IS NOT ALLOWED - tuple is immutable

# Find number of items and indexes
letter_tuple = ('a', 'p', 'p', 'l', 'e')
print("Number of p's in letter_tuple:", letter_tuple.count('p'))
print("Position of 'l' in letter_tuple:", letter_tuple.index('l'))

# Get items from a tuple and assign to variables - must match
name, age, city = mytuple
print("Info:", name, age, city)

# Get the first index as an int variable, the second to last as a list, and the last as an int variable
long_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = long_tuple

print("Partial list:", i2)

# Tuples are smaller than lists
size_list = [0, 1, 2, 3, "hello", True]
size_tuple = tuple(size_list)

print("List size:", sys.getsizeof(size_list), "bytes")
print("Tuple size:", sys.getsizeof(size_tuple), "bytes")

# Tuples are also quicker to create

print("List average creation time:", timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print("Tuple average creation time:", timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
