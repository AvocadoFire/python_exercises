# Exercise from www.pythonpractice.org
#
# Ask for a number and determine if prime. (Functions practice)

def get_integer():
    return int(input("Give me a number: "))

def check_prime(check):
    prime = 0
    for i in range(2, check-1):
        if check % i == 0:
            prime += 1
    if prime > 0:
        print("Not prime")
    else:
        print("Prime")
            

   
while True:
    check = get_integer()
    check_prime(check)
