# Strings: IMMUTABLE (unlike java), " and ' have the same effect

# Create a string and print it
my_string = "Hello World"
print("My string:", my_string)

# Use escape characters to print test
escape_string = 'I\'m a programmer!'  # other common escape characters are \n, \", \\, \b (backspace), \t (tab)
print(escape_string)

# Multi line strings (also used for documentation)
# NOTE: the \ says to continue in another line but not break lines
multi_line_string = """
Hello \
World!
I am the programmer.
"""
print(multi_line_string)

# Access a character from the string
print("First letter in", my_string, my_string[0])
# my_string[0] = 'e' DOES NOT WORK as strings are immutable

# Print the string horizontally with single quotes between each letter
for char in my_string:
    print("'", char, "' ", sep="", end="")

# Create a substring - INCLUSIVE AT BEGINNING, EXCLUSIVE AT END (don't forget) - same as a list
print("\nSubstring:", my_string[2:10])
print("\nSubstring every other character:", my_string[2:10:2])  # Use a step index to print every other character

my_string[::-1] # Reverses string but has no effect (not assigned to anything)

# Concatenate strings
greeting = "Hello"
name = "Bill"
sentence = greeting+" "+name
print(sentence)  # Note that print(...) uses COMMAS to concatenate

if "ill" in sentence:
    print("There is an 'ill' in sentence variable")

# Strip off whitespace
whitespace_string = "                Hello World             "
print("Whitespace:", whitespace_string)
no_whitespace_string = whitespace_string.strip()  # NOTE: whitespace_string.strip() by itself does NOT change whitespace_string
print("No whitespace:", no_whitespace_string)

# Convert to uppercase - does not change string
print("Upper case:", my_string.upper(), "\nLower case:", my_string.lower())

# Check if a string starts/ends with a specific string or substring
print(sentence, "starts with H:", sentence.startswith("H"))  # True - 'H' in 'Hello'
print(sentence, "starts with Bill:", sentence.startswith("Bill"))  # False - does not start with 'Bill'
print(sentence, "ends with Bill:", sentence.endswith("Bill"))  # True - ends in 'Bill'

# Find a substring/character in a string - returns -1 if does not find
print("Sentence index of 'l':", sentence.find("l"))
print("Sentence index of 'llo':", sentence.find("llo"))  # These two will be the same - it detects the first 'l'

# Count characters in a string
print("Num of 'l's in sentence:", sentence.count("l"))

# Replace a word in a string - note: DOES NOT CHANGE THE TARGET STRING
print("Replaced 'Bill' in sentence:", sentence.replace("Bill", "Steven"))

# Split a sentence into a list of words
sentence_list = sentence.split()
print("Sentence split into list of words:", sentence_list)  # You can change the delimeter to something else you want (as an argument)

# Convert a list of strings back into a string - the starting string is what is in between the items in the list
print("Joined sentence", " ".join(sentence_list))

# Create a string of a long amount of repeating digits
my_list = ['a'] * 60  # Create a list with 60 a's
long_string = ''.join(my_list)
print("Repeated string:", long_string)

# Format a string
# Old way below
name1 = "Steven"
name2 = "Peter"

# Put in a string
my_string = "%s was a member of 11115 Gluten Free" % name1
print(my_string)

# Put in a float value
variable = 2.718282828  # 2.718281828459045235374760
my_string = "The variable is %.2f" % variable  # Use %d for ints and %f for floats
# - for %f you can do .n for some number of decimal values, will round properly!!!
print(my_string)

# Newer way

my_string = "{} and {} were members of 11115 Gluten Free".format(name1, name2)
print(my_string)

# Use decimal rounding
my_string = "The variable is {:.3f}".format(variable)  # use the colon, and then the decimal point
print(my_string)

# Newest way - f-string (faster than previous methods actually)

my_string = f"{name1} and {name2} were members of 11115 Gluten Free"
print(my_string)

print(f"The variable is {variable}.") # You can also use it in line as a print statement
