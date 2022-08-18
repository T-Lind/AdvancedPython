import random
import secrets

# Random is actually pseudorandom if you want to define a seed, otherwise it's closer to true random but still not
# 'secrets' is true random though
random.seed(42)

# Get a random number 0-1
a = random.random()
print("Random num 0-1:", a)

# Get a random float from 1-10
a = random.uniform(1, 10)
print("Random float 0-10:", a)

# Get a random int from 1-10 (inclusive on both ends)
a = random.randint(1, 10)
print("Random int 1-10:", a)

# Get a random int from 1-10, exclusive on the end
a = random.randrange(1, 10)
b = random.randrange(1, 10)
print("Random num 1-10, 10 not included:", a, b)  # Note that these numbers are the same because the seed is set

# Create a normal distribution RNG
a = random.normalvariate(0, 1)  # mean of 0 and standard deviation of 1
print("Random num with a normal distribution 0-1:", a)

# Get a random item from some data type
mylist = list("ABCDEFGH")
a = random.choice(mylist)
print("Random element in first eight letters:", a)

# Get a random sample of some amount from a data type
a = random.sample(mylist, 3)  # 3 samples, each is unique
print("3 random samples:", a)

# Get a random sample of some amount from a data type, but WITH REPEATING VALUES
a = random.choices(mylist, k=3)  # k= # of samples, could be ['F', 'A', 'F'] for example
print("3 random samples w/ possibility of repeats:", a)

# Shuffle a list randomly - mutable datatypes!
random.shuffle(mylist)  # Rearrange the order of elements randomly
print("Randomly rearranged letters:", mylist)

# Use the 'secrets' module - true random outputs

# Generate a true random number 0-10, exclusive on upper bound
a = secrets.randbelow(10)
b = secrets.randbelow(10)
print("True random numbers:", a, b)

# Return an integer with k random bits
a = secrets.randbits(4)  # highest possible number is 1111 which is 15
print("Random bits = 4:", a)

# Use secrets to perform a random choice from a list, not reproducible like all other secret functions
a = secrets.choice(mylist)
print("Random choice:", a)
