# Write a program to filter a list of numbers which are divisible by 5. 

def isDivisibleByFive(x):
    if(x % 5 == 0):
        return True
    return False

l = [1, 25, 456, 566785, 58, 999, 45, 66789925]

print(list(filter(isDivisibleByFive, l)))