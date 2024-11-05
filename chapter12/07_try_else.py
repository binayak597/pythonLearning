# Sometimes we want to run a piece of code when try will successful. 

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:
    print("I am inside else") # else clause will only exceute when the try will execute successfully without throwing any error