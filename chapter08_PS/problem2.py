# Write a python program using function to convert Fahrenheit to Celcius.

#c = 5 * (f - 32) / 9

def f_to_c(f):

    return 5 * (f - 32) / 9


f = int(input("Enter the value: "))

result = f_to_c(f)

print(f"converted value of fahrenheit {f} to celcius is {round(result, 2)} degree celcius")