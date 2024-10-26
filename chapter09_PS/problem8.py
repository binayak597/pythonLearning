# Write a program to make a copy of a text file “this. txt” 

with open("this.txt", "r") as file:
    content = file.read()

with open("this_copy.txt", "w") as file:
    file.write(content)