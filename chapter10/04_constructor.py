class Employee:

    #class attribute
    language = "Python"
    salary = 120000


    # constructor

    def __init__(self, name, salary, language):  # it's a dunder method that gets called only once when an object gets initiated

        # these are the instance attributes to an object
        self.name = name
        self.salary = salary
        self.language = language

        print("hey i am a constructor")

    
    # instance methods

    def getInfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")

    # class method

    @staticmethod
    def greet():
        print("hello")

a = Employee("Binayak", 130000, "Javascript")
print(a.name, a.salary, a.language)

a.getInfo()
a.greet()