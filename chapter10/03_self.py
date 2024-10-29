class Employee:

    # class attributes
    language = "Python"
    salary = 120000


    #instance method
    
    def getInfo(self):
        print(f"the salary is {self.salary} and the language is {self.language}")
    

    # class methods
    @staticmethod
    def greet():
        print("hello")
    


a = Employee()

a.getInfo()
a.greet()


# we cannot directly access instance methods inorder to access this we need to call those methods using an obj and as a default parameter we need to pass "self" as a first argument so that function can figure it out that it is calling on which obj context and accordingly it will return the value of attibutes respected to that obj

# while in case of class methods you need to use "@staticmethod" decorator to a method so that you dont need to pass "self" as the argument because it belongs to class not to obj

#still we will call that staticmethod with the help of obj but that belong to class not to obj

# self is a keyword that represent the current instance of the class but this is just a placeholder so you can use any name as you want but if you will change that name to anyname then you have to also change in all occurance of "self" inside that method as well just like this

# However, using "self" is a standard practice for readability and consistency.

# def getInfo(self):
#         print(f"the salary is {self.salary} and the language is {self.language}")

# if you want to give any name instead of "self" then you need to write like this

# def getInfo(pubg):
#         print(f"the salary is {pubg.salary} and the language is {pubg.language}")