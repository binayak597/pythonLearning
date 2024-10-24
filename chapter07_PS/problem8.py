# Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 

num = int(input("Enter the number: "))
# calculative method

for i in range(1, num + 1):
    print(i * "*")


# variable method

# stars = 1

# for i in range(1, num + 1):
#     print(stars * "*")
#     stars += 1
