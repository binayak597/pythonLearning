class Employee:
    # you can define as many class atrributes here depend on your requirement

    language = "Python"
    salary = 120000


e = Employee() # create an obj of Employee class

e.name = "Binayak" #this one represents object / instance attribute
# similarly you can create as many instance attributes for an object as well

print(e.name, e.language, e.salary)


# so whenever you want to create an instance attribute you can create using an object but when you want to create a class attribute you can create inside class because they are belong to class