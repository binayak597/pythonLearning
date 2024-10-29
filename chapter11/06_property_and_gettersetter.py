# class Circle:
#     def __init__(self, radius):
#         self._radius = radius  # Notice the underscore to indicate a "private" attribute

#     @property
#     def radius(self):
#         """Getter for radius property"""
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         """Setter for radius property with validation"""
#         if value < 0:
#             raise ValueError("Radius cannot be negative")
#         self._radius = value

#     @property
#     def area(self):
#         """Read-only property for area, calculated based on radius"""
#         return 3.14159 * (self._radius ** 2)

# # Example usage
# c = Circle(5)
# print(c._radius)
# print(c.radius)      # Accessing radius (getter)
# c.radius = 10        # Setting radius (setter)
# print(c._radius)
# print(c.area)        # Accessing area (read-only property)
# # c.radius = -3      # Would raise ValueError: Radius cannot be negative


class Employee:

    company = "Microsoft"

    # getter method by property decorator
    @property
    def name(self):
        return f"{self.fName} {self.lName}"
    
    @name.setter
    def name(self, value):

        self.fName = value.split(" ")[0]
        if(value.split(" ")[1] == "Mukherjee"):
            self.lName = "Rogers"


a = Employee()

print(a.company)

a.name = "Binayak Mukherjee"

print(a.name)

print(a.fName, a.lName)