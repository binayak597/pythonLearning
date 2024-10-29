# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:

    # class attribute
    a = 4

o = Demo()

print(o.a) # print the class attribute value because there is no instance attribute "a" is present in this obj

o.a = 2 # set the instance attribute "a" value to 2

print(o.a) # print the instance attribute but its not going to change the class attribute value

print(Demo.a)