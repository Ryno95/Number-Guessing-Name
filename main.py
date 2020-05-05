# Build a guessing game, generate a random number between 1 and 20 where
# The player inputs a number, if wrong tell the user to guess higher or lower
# game ends when user types exit or if player guesses correctly
# keep track of the amount of guesses

import random

# ----- Global Variables ------
startingNum = random.randint(1, 20)


# ----- Functions -------


def mainGame():
    userInput = input("Choose a number between 1 and 20: ")
    count = 1
    gameIsActive = True

    while gameIsActive:
        if str(userInput) == "exit":
            print("Game exited!")
            break
        elif startingNum > int(userInput):
            userInput = input("Your number was too low, guess again!: ")
        elif startingNum < int(userInput):
            userInput = input("Your number was too high, guess again!: ")
        else:
            print(f"Game won! You guessed {count} times")
            gameIsActive = False
        count += 1


mainGame()
