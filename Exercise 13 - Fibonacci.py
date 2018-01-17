# Exercise from www.pythonpractice.org
#
# Generate fibonacci numbers in range given by user

# Get input
def userinput():
    return int(input("Enter a number: "))

def fibonacci(generate):
    a = [0,1]
    b = []
    x = 0
    for i in range(1,generate-1):
        if i < generate:
            x = a[-2] + a[-1]
            a.append(x)
        else:
            break
    for i in a:
        if i < generate:
            b.append(i)
    print (b)

while True:
    generate = userinput()
    fibonacci(generate)
    
    




