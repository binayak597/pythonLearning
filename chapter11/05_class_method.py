class Employee:

    a = 1

    @classmethod
    def show(cls):
        print(f"hey your value is {cls.a}")

e = Employee()
e.a = 45
e.show()