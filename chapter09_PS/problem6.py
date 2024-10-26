# Write a program to mine a log file and find out whether it contains ‘python’.

with open("log.txt", "r") as file:
    content = file.read()

if("python" in content):
    print("Yes python is present in this file")
else:
    print("No python is not present in this file")