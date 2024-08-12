#a program that generates a random number. The user wins if he/she guesses the number correctly, otherwise he/she keeps trying, following the clues. The number of tries are displayed on the Correct guess, the user with least number of guesses wins the game.

import random

target= random.randint(1,100)
# print(target)
tries=0
#asking user to guess the Number, Until he/she guesses Right
while True:
    tries+=1
    userChoice = input("Guess the target or Quit(Q): ")
    if(userChoice=="Q" or userChoice=="q"):
        break

    userChoice=int(userChoice)
    if (userChoice == target):
        print("You have guessed successfully in",tries,"tries!")
        break
    elif(userChoice<target):
        print("OOPS! Your number was too small. Take a bigger Guess.")
    else:
        print("OOPS! Your number was too large. Take a smaller guess.")


print("-------GAME OVER------_")
