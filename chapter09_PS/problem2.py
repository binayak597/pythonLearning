# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing a game....")

    # generate e random number
    score = random.randint(1, 60)

    print(f"Your score is: {score}")
    # fetch the score from the Hi-score.txt file
    with open("Hi-score.txt", "r") as file:
        hiscore = file.read()

        # wheather we are writing or reading from file it will always give us data in string format
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    # compare the scores
    if(score > hiscore):

        # update the file with new score
        with open("Hi-score.txt", "w") as file:
            file.write(str(score))

    
    return score

game()