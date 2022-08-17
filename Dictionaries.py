# Dictionaries - like hashmaps in Java, use curly braces. Mutable object

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# Another way of defining a dictionary - here I'm defining a dictionary in a dictionary
mydict2 = dict(name="Mary", age=27, city="Boston", husband=dict(name="Bill", age="29", city="Boston"))
print(mydict2)

# Get a value - input key as a string and get the value
print(mydict2["name"], "'s husband is", mydict2["husband"]["name"], sep="")

# All immutable items can be keys - ex. NOT lists, but tuples works
mydict2[0] = "number"
print("Dict with number as a key", mydict2)

# Delete an item
del mydict2[0]
print("New dict:", mydict2)

# Pop an item to use (removes it and returns it)
print("Husband popped:", mydict2.pop("husband"))

mydict2["Favorite food"] = "Ice cream"

# Use popitem to remove the last inserted item
print(mydict2.popitem())

# Print an item if it's in the dict
if "name" in mydict:
    print("mydict name:", mydict["name"])

# try except block does the same
try:
    print("mydict name:", mydict["name"])
except:
    print("Error")

# Loop through dictionary

for key in mydict: # or, 'for key in mydict.keys()' also works
    print(key, mydict[key])

# Get all the values in the dictionary
for value in mydict.values():
    print(value)

# Also works
for key, value in mydict.items():
    print(key, value)

# Dictionaries also use aliases when copying
dict_deep_cpy = mydict.copy()
dict_deep_cpy["Profession"] = "Banker"
print(dict_deep_cpy)

# Combine dictionaries - KEYS ARE OVERRIDDEN by whatever's in update(...)
mydict.update(mydict2)
print(mydict)


