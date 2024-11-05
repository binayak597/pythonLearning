
# traditional way

n = [1, 2 ,3, 4]
if(len(n) > 5):
    print("heeyyyy")
else:
    print("hello")


# using walrus operator we can write these line of codes as a single expression

if(n := len([1, 2, 3, 4])) > 5:
    print("heyyy")
else:
    print("hello")

print(n)


while (line := input("Enter a word: ")) != "quit":
    print(f"You entered: {line}")

print(line)