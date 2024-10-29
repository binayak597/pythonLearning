class Employee:

    company = "ITC"
    name = "Default name"
    language = "Python"

    def getInfo(self):
        print(f"your name is {self.name} and your company is {self.company}")


class Coder:

    language = "Javascript"

    def printLanguage(self):
        print(f"your fav language is {self.language}")


class Programmer(Employee, Coder): # because we are passing multiple classes so in this case ordering matters as respected to retreival operation

    company = "ITC Infotech"

    def showLanguage(self):
        print(f"your company name is {self.company} and your laguage is {self.language}")


a = Programmer()

a.showLanguage() # your company name is ITC Infotech and your laguage is Python

a.printLanguage() # your fav language is Python

a.getInfo() # your name is Default name and your company is ITC Infotech