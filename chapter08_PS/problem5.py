# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 

def printPattern(num):

    if(num == 0):
        return
    
    print(num * "*")
    printPattern(num - 1)


num = int(input("Enter the number: "))
printPattern(num)