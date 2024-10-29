class Employee:

    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"your name is {self.name} and your salary is {self.salary}")


class Programmer(Employee):

    # company = "ITC Infotech"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


a = Employee("Binayak", 120000)
a.show()

b = Programmer("Rajesh", 50000)
print(b.company)

# if we talk about the preference level

# instance attribute > class attribute > (if that class inheriting from any other class then that class attribute)

b.show()