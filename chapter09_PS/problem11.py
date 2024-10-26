# Write a python program to rename a file to “renamed_by_ python.txt. 

with open("old.txt") as file:
    content = file.read()

with open("renamed_by_python.txt", "w") as file:
    file.write(content)