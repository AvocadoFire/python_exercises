# Make a one-player Rock-Paper-Scissors game.
# TODO: Abstract out Win, Lose, Draw conditions
import random

print("Lets play rock paper or scissors. It will be thrilling.\n")

options = ["R","P","S"]

# Choose random from options for computer's guess
a = random.randint(0,2)
computer = options[a]

# Prompt player to choose
p1 = input("(R)ock, (P)aper, or (S)cissors?")

while p1 == "R":
    if computer == "R":
        print ("A draw! Inconceivable!")
        break
    elif computer == "P":
        print ("You were defeated by a random number generator. Welcome to the future.")
        break
    elif computer == "S":
        print ("Congratulations. No really, well done. Well done, you")
        break

while p1 == "S":
    if computer == "S":
        print ("A draw! Inconceivable!")
        break
    elif computer == "R":
        print ("You were defeated by a random number generator. Welcome to the future.")
        break
    elif computer == "P":
        print ("Congratulations. No really, well done. Well done, you")
        break

while p1 == "P":
    if computer == "P":
        print ("A draw! Inconceivable!")
        break
    elif computer == "S":
        print ("You were defeated by a random number generator. Welcome to the future.")
        break
    elif computer == "R":
        print ("Congratulations. No really, well done. Well done, you")
        break

        
        
        


  
    



        


