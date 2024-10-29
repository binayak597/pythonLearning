# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.


class Demo:

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # instance method
    def giveName(self):
        print(f"Your name is {self.name}")

    #using another name instead of self keyword
    def giveSalary(slf):
        print(f"Your salary is {slf.salary}")


a = Demo("Binyak", 120000)
a.giveName()
a.giveSalary()