# Write a program to calculate the factorial of a given number using for loop.


# ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

num = int(input("Enter the num: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)