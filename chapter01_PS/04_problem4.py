# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  


import os

# os is the built in module in python

# Select the directory whose content you want to list 
directory_path = '/' # this one will give you contents of c drive bydefault


# directory_path='D://' 
# for a specific directory ex: -> "D directory"

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)