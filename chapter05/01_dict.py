d = {} # Empty dictionary

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}


print(marks, type(marks))
print(marks["Harry"])

#in dict when we try to access a particular key corresponding value we need to write the syntax something like that marks[<"key">] so in this case dict not scan the entire dict to find out the key and then return its value instead it calculates the location of that given key and return its value in O(1) time