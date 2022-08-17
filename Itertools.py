# Itertools: iterators that can be used in a loop

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator

# Use product to compute the cartesian product of two lists - groups items into a tuple
a = [1, 2]
b = [3]
prod_rep_1 = product(a, b, repeat=1)
prod_rep_2 = product(a, b, repeat=2)
print("Repeat=1",list(prod_rep_1))  # Convert the itertools object to a list
print("Repeat=2",list(prod_rep_2))  # Convert the itertools object to a list

# Use permutations to return all possible orderings of an input - repeated inputs are counted as separate items
c = [1, 2, 3]
perm = permutations(c)
print(f"Permutations of {c}:", list(perm))

perm_2 = permutations(c, 2)
print(f"Permutations of {c}:", list(perm_2))  # Permutations with a length of 2

# Combinations: Make all possible combinations of a specified length - no matching pairs
d = [1, 2, 3, 4]
comb = combinations(d, 2)
print(f"Combinations of {d}:", list(comb))  # Combos with a length of 2

# Combinations with replacement - successive length matches including matching pairs
comb_wr = combinations_with_replacement(d, 2)
print(f"Combinations w/ replacement of {d}:", list(comb_wr))  # Combos wr with a length of 2

# Accumulate - kind of like a snowball with numbers, default is add but you can use operator.mul to multiply each element
acc = accumulate(d, func=operator.mul)  # use func=max for an array filled with the current largest number up to that point
print("Accumulate input:", d)
print("Accumulate output:", list(acc))

# Groupby - makes an iterator that returns groups and keysit
