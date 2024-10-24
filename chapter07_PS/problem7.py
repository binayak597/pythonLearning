# Write a program to print the following star pattern. 
#  * 
# *** 
#***** for n = 3


num = int(input("Enter the number: "))
# calculative method

# for i in range(1, num + 1):
#     print((num - i) * " ", end="") # end="" this empty string represent blank 
#     print((2 * i - 1) * "*", end="")
#     print()


# variable method

stars = 1
spaces = num - 1

for i in range(1, num + 1):
    print(spaces * " ", end="")
    print(stars * "*", end="")
    stars += 2
    spaces -= 1
    print()
