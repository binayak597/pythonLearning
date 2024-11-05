# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module.


from random import randint


def guessNumber():

    randomNumber = randint(1, 100)

    count = 1

    userGuess = int(input("Guess a number between 1 to 100... "))


    while(randomNumber != userGuess):

        if(userGuess < randomNumber):
            userGuess = int(input("You Entered the lower number\ntry again... "))
            
        elif(userGuess > randomNumber):
            userGuess = int(input("You Entered the highest number\ntry again... "))

        elif(userGuess == randomNumber):
            break

        count += 1
    
    print(f"You have taken {count} no of attempt to guess the random number {randomNumber}")
            

guessNumber()