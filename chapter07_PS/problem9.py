# Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  


num = int(input("Enter the number: "))

# calculative method

for i in range(1, num + 1):
    if( i == 1 or i == num):
        print(num * "*")
    else:
        print("*", end="")
        print((num - 2) * " ", end="")
        print("*")
