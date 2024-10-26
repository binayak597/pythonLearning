

f = open("file.txt", "r") 

# as the first argument to open method you need to pass the filename along with its location starting from the current executing directory

# by default it povides read mode so its optional if you don't want to wrtie "r" mode as the second argument
data = f.read()
print(data)
f.close()