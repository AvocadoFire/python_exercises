# 1. Generate a random number between 1 and 9.
# 2. Ask the user to guess the number, then tell them if they are low, high or right

import random
print("Guess a number between 1 and 9 or type 0 to exit\n")
a = random.randint(1,9)
guesscount = 1

while True:
    guess = int(input("Guess: "))
    if guess == a:
        print("You got it in",guesscount,"!")
        break
    elif guess == 0:
        break
    elif guess < a:
        print("Too low")
        guesscount += 1
    elif guess > a:
        print ("Too high")
        guesscount += 1
