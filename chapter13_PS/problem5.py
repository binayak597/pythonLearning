# Write a program to find the maximum of the numbers in a list using the reduce 
# function.

from functools import reduce

l = [20, 200, 197, 46787, 40000, 56]

def findMax(a, b):
    if a > b:
        return a
    return b

ans = reduce(findMax, l)

print(ans)