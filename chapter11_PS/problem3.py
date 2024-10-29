#  Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary. 


class Employee:

    salary = 5000
    increment = 20


    @property
    def salaryAfterIncrement(self):
        return (self.salary + (self.salary * (self.increment / 100)))
    

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, newSalary):

        self.increment = ((newSalary - self.salary) / self.salary) * 100
a = Employee()
# print(a.salaryAfterIncrement())

a.salaryAfterIncrement = 7000
print(a.increment)