# Lists are mutable and repeatable data is allowed

mylist = [1, 9, 3, 0, -4]

# Print the list
print("List:", mylist)

# Print the second to last item
print("Second to last item:", mylist[-2])

if 0 in mylist:
    print("There is a zero in myList")
else:
    print("There is no zero in myList")

# Reverse list
mylist.reverse()
print("Reversed list:", mylist)

# Sort my list
sorted_list = sorted(mylist)
print("Sorted list:", sorted_list)

# Create a list of 5 zeroes
zeroes = [0] * 5
print("List of 5 zeroes:", zeroes)

# Combine lists
summed_list = mylist + zeroes
print("Summed list:", summed_list)

# Take a partial list - last # is the step
partial_list = summed_list[2:9:2]
print("Partial list 2-9 step 2", partial_list)

# ASSIGNING A LIST LIKE THIS CAUSES AN ALIAS - BOTH LIST VARIABLES POINT TO THE SAME LIST
lists_org = ["banana", "cherry", "apple"]

# Alias copying
list_alias_cpy = lists_org

# Deep copying
list_deep_cpy = lists_org.copy() # list(list_org) and list_org[:] also create actual copies

# Show the difference between copying
lists_org.append("lemon")

print("Original list", lists_org)
print("Alias copy", list_alias_cpy)
print("Deep copy", list_deep_cpy)

# Perform an operation to every element in a list
mylist_squared = [i*i for i in mylist]
print("Squared list: ", mylist_squared)


