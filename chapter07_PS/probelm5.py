# Write a program to find the sum of first n natural numbers using while loop. 


num = int(input("Enter the number: "))

sum = 0
i = 1

while(i <= num):
    sum += i
    i += 1

print(sum)