from functools import reduce
# Map Example 
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)

print(sqList) # it will return us an map obj address
print(list(sqList)) # it will return us the data in a list

# Filter Example
def even(n):
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, l)
print(list(onlyEven))

# Reduce Example
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))