# Exercise 18 from www.pythonpractice.org

# Randomly generate a 4-digit number.
import random
num = random.randint(1000,9999)

# Ask the user to guess the number.
def getinput():
    a = 0
    while a < 1000 or a > 9999:
        a = int(input("I'm thinking of a number between 1000 and 9999...: "))
    return a

# Access and assess the numbers with cows or bulls
def access(num,guess):
    a = str(num)
    b = str(guess)
    c = 0
    d = 0
    for i in range(0,4):
        if a[i] == b[i]:
            c += 1
        else:
            d += 1
    return c, d

if __name__=="__main__":
    cows = 0
    bulls = 0
    loops = 0
    while True:
        # Keep track of the number of guesses and tell the user at the end
        loops += 1
        guess = getinput()
        cows,bulls = access(num,guess)  
        print(cows,bulls)
        # Once the user guess the correct number, the game is over
        if cows == 4:
            print("Win! It took you",loops,"guesses")
