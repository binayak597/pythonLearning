
result1 = "{} is a good {}".format("Binayak", "boy")
print(result1)

result2 = "{0} is a good {1}".format("Boy", "Binayak")
print(result2)

result3 = "{1} is a good {0}".format("Boy", "Binayak")
print(result3)


#by default format method follows the default ordering of the parameters but if we pass based on indices then accordingly those values would replace the brackets