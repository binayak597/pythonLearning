
# its a modern way of deal with files in python with "with" keyword
# which will open and close the file automatically
# it provides a very simpler syntax inorder to work with file system i/o

# traditional way
f = open("file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("file.txt") as file:
    print(file.read())

# You dont have to explicitly close the file