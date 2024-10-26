# Write a program to find out whether a file is identical & matches the content of 
# another file. 

with open("this.txt", "r") as file:
    content1 = file.read()

with open("this_copy.txt", "r") as file:
    content2 = file.read()

if(content1 ==content2):
    print("Yes both files are identical")
else:
    print("No both files are not identical")