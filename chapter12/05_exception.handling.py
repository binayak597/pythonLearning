# this code will generate error and disrupt the normal flow of execution

# a = int(input("Enter a number: "))

# print(a)

# print("heyyy")

# with the help of try except clause

# try:
#     a = int(input("Enter a number: "))
#     print(a)
# except Exception as e:
#     print(e)

# print("heyyy")


try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as v:
    print(v)
    print("hello")

except Exception as e:
    print(e)

print("heyyy")
