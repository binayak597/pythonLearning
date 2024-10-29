# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         """Overloads the + operator to add two vectors."""
#         return Vector(self.x + other.x, self.y + other.y)

#     def __repr__(self):
#         """Defines the string representation of the Vector object."""
#         return f"{self.x}i + {self.y}j"

# # Example usage
# v1 = Vector(2, 3)
# v2 = Vector(5, 7)
# v3 = v1 + v2  # This calls v1.__add__(v2)
# print(v3)     # Output: 7i + 10j


class Number:

    def __init__(self, num):

        self.num = num

    
    # def __add__(self, other): # dunder or magic method

    #     return Number(self.num + other.num)
    
    def __add__(self, other): # dunder or magic method

        return self.num + other.num
    

    # def __str__(self):
    #     return f"{self.num}"

a = Number(5)
b = Number(6)

print(a + b) # it will internally call a.__add__(b)