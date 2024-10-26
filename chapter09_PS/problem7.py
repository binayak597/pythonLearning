# Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "r") as file:
    lines = file.readlines()


lineno = 1

for line in lines:
    if("python" in line):
        print(f"Yes python is present at line no {lineno}")
        break
    lineno += 1
else:
    print("No python is not present in this file")

# in python "for with else statement" if you are using then you need to know some concept 
# after for loop execution will over or for loop will exhaust then this else block will execute 
# if inside for loop you have written break keyword so as soon as this break keyword will execute the control flow will comeout from the innermost loop but the else block will not execute