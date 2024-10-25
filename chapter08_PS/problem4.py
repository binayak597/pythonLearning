# Write a recursive function to calculate the sum of first n natural numbers.

'''
sum(0) = 0
sum(1) = 0 + 1
sum(2) = 0 + 1 + 2
sum(3) = 0 + 1 + 2 + 3
sum(4) = 0 + 1 + 2 + 3 + 4
sum(5) = 0 + 1 + 2 + 3 + 4 + 5

sum(n) = 0 + 1 + 2 + 3 + 4 + .... + n -1 + n
sum(n) = sum(n-1) + n

'''



def sum(n):
    if(n == 1 or n == 0):
        return n
    return n + sum (n-1)


num = int(input("Enter the number: "))

result = sum(num)

print(f"the sum of first {num} natural number is {result}")
    