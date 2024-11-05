#  Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 

l = [1, 2, 3, 4, 5, 6 ,7, 8]

for idx, item in enumerate(l):
    if(idx == 2 or idx == 4 or idx == 6):
        print(item)