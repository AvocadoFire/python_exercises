# Exercise from www.pythonpractice.org
#
# PW Generator

import random

def main():
    print("### PW Generator V1.0 ###\n")
    print("Type 1 for a weak password")
    print("Type 2 for a strong password")
    print("Type anything else to quit")
    weaklist = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',]
    stronglist = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z','A',
                 'B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                  'P','Q','R','S','T','U','V','W','X','Y','Z','0','1',
                  '2','3','4','5','6','7','8','9','0','!','£','$','%','^',
                  '&','*','(',')']
    choice = menu()
    while True:
        if choice == '1':
            p1 = weak(weaklist)
            print (p1)
        elif choice == '2':
            p2 = strong(stronglist)
            print (p2)
        else:
            break

def menu():
    return input(": ")

def weak(weaklist):
    length = int(input("How many letters?: "))
    a = []
    for i in range(0,length):
        x = random.randint(1,25)
        a.append(weaklist[x])
    return ''.join(a)


def strong(stronglist):
    length = int(input("How many characters? (Must be 10 or over): "))
    while length < 10:
        length = int(input("How many characters? (Must be 10 or over): "))
    a = []
    for i in range(0,length):
        x = random.randint(1,70)
        a.append(stronglist[x])
    return ''.join(a)
    

if __name__ == "__main__":
    main()









    
