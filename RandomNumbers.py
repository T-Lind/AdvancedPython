import random

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
print("Random num 1-10, 10 not included:", a)

# Create a normal distribution RNG
a = random.normalvariate(0, 1)
print("Random num with a normal distribution 0-1:", a)


