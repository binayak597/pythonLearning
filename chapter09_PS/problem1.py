# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

with open("poem.txt", "r") as file:
    result = file.read()
    if("twinke" in result):
        print("Yes Twinkle is present in this file")
    else:
        print("No Twinkle is not present in this file")