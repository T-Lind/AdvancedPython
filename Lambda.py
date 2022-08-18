# Lambda - function without a name expressed as 'lambda arguments: expression' all in one line. Can assign to a variable

# Create a lambda function to add 10 to the input, and print an input of 5
from functools import reduce

add10 = lambda x: x + 10
print("add10(5):", add10(5))

mul = lambda x, y: x * y
print("mul(2, 7):", mul(2, 7))

# Sort values according to the x using the default sorted() method which sorts to the first parameter, and then according
# to the second using the lambda expression to sort y's
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted_x = sorted(points2D)
points2D_sorted_y = sorted(points2D, key=lambda x: x[1])

print("Points sorted by x:", points2D_sorted_x)
print("Points sorted by y:", points2D_sorted_y)

# Sort values according to the sum of the x and y
points2D_sorted_sum = sorted(points2D, key=lambda tup: tup[0] + tup[1])  # note that x is not the x value but the TUPLE!

print("Points sorted by sum:", points2D_sorted_sum)

# Map a lambda expression to each value in the list - applies the function to every value. Can be done with list comprehension.
# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))
# above is same as
# c = [x*2 for x in a]

# Find the even values in list a and put them in a new list
b = filter(lambda x: x % 2 == 0, a)  # same as [x for x in a if x%2 == 0]
print("Even values:", list(b))

# Print the sum of everything in list a
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
