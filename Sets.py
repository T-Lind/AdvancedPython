# Sets: unordered, mutable, no duplicates

# NO KEYS - what makes it syntactically different from a dictionary
myset = {1, 2, 3, 1, 3, 2}
print(myset)

# Convert a string to a set
word_set = set("Hello")
print("Word set", word_set)  # Note the order is arbitrary!

# Convert a list to a set
item_set = set([True, 3, 9, 3, 0])
print("Item set", item_set)

# Create an empty set
empty_set = set()  # NOTE: empty_set = {} DOES NOT WORK because it defaults to a dictionary

item_set.add(1)
item_set.discard(3)  # item_set.remove(10) would throw an error because 10 does not exist - discard does not throw errors
print("Edited set", item_set)

# Combine sets
print("Union set", word_set.union(item_set))

# Find common elements between two sets
print("Common elements", item_set.intersection(myset))

# Calculate the difference between sets - things that are in set A but not B
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_b = {1,    3,       6,       9, 11}

print("A/B difference", set_a.difference(set_b)) # Will not modify set, but return a new set
print("B/A difference", set_b.difference(set_a)) # Will not modify set, but return a new set

# Find the symmetric difference - essentially the union of both sets above
print("Symmetric difference", set_a.symmetric_difference(set_b)) # Works the same both ways around - will not modify set

# Combine two sets but do not return a new set - edit existing one
myset.update(set_b)

# Only keep elements found in both sets - does not return value
set_a.intersection_update(set_b)
print("Intersection update", set_a)

# See if set c is in set a
set_a = {1, 2, 3, 4, 5}
set_c = {1, 2, 3}
print("Set a is a superset of c:",set_a.issuperset(set_c))  # same as print(set_c.issubset(set_a))

# See if no elements are in common
print("Set a and c are disjoint:", set_a.isdisjoint(set_c))

# Properly copy a set
set_d = set_a.copy()
