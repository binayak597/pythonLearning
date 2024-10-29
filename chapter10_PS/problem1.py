# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.


class Programmer:

    # class attribute
    company = "Microsoft"


    # constructor

    def __init__(self, name, salary, pin):

        self.name = name
        self.salary = salary
        self.pin = pin

    
a = Programmer("Binayak", 130000, 123456)
print(a.name, a.salary, a.pin, a.company)
b = Programmer("Harry", 120000, 123456)
print(b.name, b.salary, b.pin, b.company)