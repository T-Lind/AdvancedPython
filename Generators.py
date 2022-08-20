import sys


# Generators - functions that return an object that can be iterated over, generate items inside the object lazily (one
# at a time and only when you ask for it)

def mygenerator():
    yield 3
    yield 2
    yield 1


g = mygenerator()

val = next(g)  # Pops the yield value out
print("Gen output:", val)

val = next(g)
print("Gen output:", val)

g = mygenerator()  # Note that since it pops the stuff out then I have to redefine it every time I want the inputs back again

# Raises a StopIteration if it doesn't encounter another yield statement

print("Generator sum:", sum(g))  # Output is 6

g = mygenerator()

print("Generator sorted:", sorted(g))


# Infinite series generator because Kavin asked for it
def generator():
    x = 0
    while True:
        x += 1
        yield x


g = generator()
print("Num 1:", next(g))
print("Num 1:", next(g))


# Count down from a number
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


# Both of these functions just do the same thing, but a lot of memory is saved!
print("Ordinary list method in bytes:", sys.getsizeof(firstn(1000)))
print("Generator method in bytes:", sys.getsizeof(firstn_generator(1000)))

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

fib = fibonacci(30)
for i in fib:
    print(f"Fib number: {i}")

# Same thing as list comprehension but uses a generator, less memory
gen = (i for i in range(10) if i % 2 == 0)

# Convert a generator to a list
list(gen)

