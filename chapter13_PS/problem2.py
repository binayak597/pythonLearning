#  Write a program to input name, marks and phone number of a student and format it 
# using the format function like below: 
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter the name: ")
marks = int(input("Enter the marks: "))
phoneNumber = int(input("Enter the phonenumber: "))

ans = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phoneNumber)

print(ans)