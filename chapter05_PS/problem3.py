# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18) # here 18 is a number
s.add("18") # here '18' is a string

print(s)