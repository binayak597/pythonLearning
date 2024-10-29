class Employee:

    # class attributes
    language = "Python"
    salary = 120000


a = Employee()
a.language = "Javascript" # instance attribute

print(a.language, a.salary)


# although i have defined a class attribute inside a class as "language" but the time when i assign this "language" attribute as a instance attribute to obj "a", so this time only for this "a" obj this "language" attribute consider as a instance attribute.

#and when we try to access any attribute using obj, python checks wheather that attribute present as a instance attribute for that obj if it is, then python give more priority to instance attribute but if it will not available then it will look for the class attribute and return its value