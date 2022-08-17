# Multiple types of collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Must import these objects
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Create a starting string
a = ["a"] * 6 + ["b"] * 4 + ["c"] * 3
string_a = ''.join(a)

print("Starting string:", string_a)

# Creates a dictionary of each letter (or item in a list/other iterable) and stores it along with the # of occurrences
counter = Counter(string_a)
print(counter)

# Print the most common element
print("Most common:", counter.most_common(1)[0][0])  # argument is # of most common items (None is all, so sorted in
# order of most common to least, index 1 is the first hash pair, index 2 is the key for the hash pair,

# Get an iterable list of elements
print("Get the elements in the counter:", list(counter.elements()))

# Named tuple - creates a class of fields x,y
Point = namedtuple('Point', 'x,y')

pt = Point(2, 3)
print("Point:", pt)
print(f"Point x:{pt.x}, y:{pt.y}")

# Ordered dictionary - normal dictionaries can remember what order their elements were inserted so not very useful
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['c'] = 2
ordered_dict['b'] = 3
ordered_dict['d'] = 4

# Prints out in the order of insertion
print(ordered_dict)

# Default dictionary - only difference is that there is a default key set if there has been no key set
d = defaultdict(int)  # Returns the default value of an integer, 0
d['a'] = 1
d['b'] = 2

print(d['c'])  # Does not raise a key error like a normal dictionary, instead prints the default value

# Deque - able to remove elements from both ends
d = deque()

d.append(1)
d.append(2)

# Append to the beginning of a deque
d.appendleft(3)
print("Deque:", d)

d.pop()  # Return and remove the last element (right side)
print("Deque (right popped):", d)

d.popleft()  # Return and remove the first element (left side)
print("Deque (left popped):", d)

d.clear()  # Cleare deque

d.extend([3, 4, 5])  # Add elements to right side
d.extendleft([0, -1, -2])  # Add elements to left side - in ORDER, SO THESE NUMBERS BECOME REVERSED
print("Deque extended", d)

# Rotate elements - positive is to the right, negative is to the left, shift by that #
d.rotate(-1)
print("Deque rotated:", d)
