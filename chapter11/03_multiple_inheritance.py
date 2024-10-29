class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # 1

o = Programmer()
print(o.a, o.b) # 1 2

o = Manager()
print(o.a, o.b, o.c) # 1 2 3