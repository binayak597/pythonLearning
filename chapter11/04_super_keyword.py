# class Demo1:

#     def __init__(self, name):
#         self.name = name
#         print("hey i am from Demo1")
#         print(f"Demo1 -> {self.name}")
#         print()

# class Demo2(Demo1):
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
#         print("hey i am from Demo2")
#         print(f"Demo2 -> {self.name} {self.salary}")
#         print()

# class Demo3(Demo2):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)
#         self.language = language
#         print("hey i am from Demo3")
#         print(f"Demo3 -> {self.name} {self.salary} {self.language}")
#         print()


# a = Demo1("Binayak")
# b = Demo2("Rajesh", 120000)
# c = Demo3("Harry", 120000, "python")


# # in python if a subclass inherite from a parent class then the subclass constructor will not automatically call its parent class constructor

# # if you want to execute parent class constructor the you need to use super keyword



