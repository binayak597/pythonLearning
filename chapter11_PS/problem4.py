# Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them. 

class Complex:

    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __add__(self, other):

        return Complex(self.r + other.r, self.i + other.i)
    
    def __mul__(self, other):
        real = (self.r * other.r) - (self.i * other.i)
        imaginary = (self.r * other.i) + (self.i * other.r)

        return Complex(real, imaginary)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    

a = Complex(1, 2)
b = Complex(3, 4)

print(a + b)
print(a * b)
