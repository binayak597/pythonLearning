# Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 


class Calculator:

    # constructor
    def __init__(self, n):
        self.n = n

    # instance methods

    def square(self):
        print(f"the sqaure of {self.n} is {self.n * self.n}")

    def cube(self):
        print(f"the cube of {self.n} is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"the square root of {self.n} is {self.n ** 0.5}")


a = Calculator(16)
a.square()
a.cube()
a.squareroot()