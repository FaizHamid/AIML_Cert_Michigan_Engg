# Tuples
# A tuple is an ordered, immutable collection of items. Tuples are defined using parentheses (), with items separated by commas.  
# Since tuples are immutable, their elements cannot be changed, added, or removed after the tuple is created.
# Tuples support various operations such as indexing, slicing, and iterating over elements.
# Tuples are commonly used to group related data together and can contain items of different data types.
                
# Examples of Tuple operations:

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)               # Output: Original Tuple: (1, 2, 3, 4, 5)          

# Tuple Indexing - Accessing individual elements in a tuple using their position (index)
print("First Element:", my_tuple[0])            # Output: First Element: 1
print("Last Element:", my_tuple[-1])            # Output: Last Element: 5

# Tuple Slicing - Accessing a subset of elements in a tuple using a range of indices
print("Sliced Tuple (2nd to 4th):", my_tuple[1:4]) # Output: Sliced Tuple (2nd to 4th): (2, 3, 4)

# Iterating over the tuple
print("Iterating over the tuple:")
for item in my_tuple:
    print(item)         

# Output:
# Iterating over the tuple:
# 1
# 2
# 3             
# 4
# 5

# Tuple Packing - Creating a tuple by packing multiple values into a single variable
packed_tuple = 10, 20, 30
print("Packed Tuple:", packed_tuple)           # Output: Packed Tuple: (10, 20, 30)

# Tuple Unpacking - Extracting individual values from a tuple into separate variables
a, b, c = packed_tuple
print("Unpacked Values:", a, b, c)              # Output: Unpacked Values: 10 20 30
# Note: Since tuples are immutable, the following operations will raise errors if uncommented:
# my_tuple[0] = 100          # This will raise a TypeError
# my_tuple.append(6)        # This will raise an AttributeError
# my_tuple.remove(3)       # This will raise an AttributeError
# End of Tuple operations       