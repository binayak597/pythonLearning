# We all have played snake, water gun game in our childhood. If you haven’t, google the 
# rules of this game and write a python program capable of playing this game with the 
# user.


#rules are

# 1 -> Snake
# -1 -> Water
# 0 -> Gun

import random

computer = random.choice([-1, 0, 1])

gameOptions = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

reversedGameOptions = {
    "s": 1,
    "w": -1,
    "g": 0
}

user = input("Enter your choice: ")
choiceNum = reversedGameOptions[user]

print(f"Computer choose {gameOptions[computer]}\nYou choose {gameOptions[choiceNum]}")

#edge case
if(computer == choiceNum): #if computer and user pass the same number
    print("Game Draw, Try Again.....")


#different possibilities
#with advanced analysis try to reduce number of lines in this game
#using the logic "choiceNum - computer"

if((choiceNum - computer == -1) or (choiceNum - computer == 2)):
    print("You Won....")
else:
    print("You Lose....")

