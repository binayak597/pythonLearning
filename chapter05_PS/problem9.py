# Can you change the values inside a list which is contained in set S?


# in Python, a set cannot contain mutable objects like lists. Lists are mutable, meaning their contents can be changed, and since sets require their elements to be hashable and immutable (i.e., unchangeable), a list cannot be an element of a set.

# If you try to include a list inside a set, you'll get a TypeError.

# If you want to store something like [1, 2] in a set, you can use a tuple instead. Tuples are immutable and hashable, making them valid elements for a set:

s = {8, 7, 12, "Harry", [1, 2]}  # This will raise an error
s = {8, 7, 12, "Harry", (1, 2)}  # This works fine