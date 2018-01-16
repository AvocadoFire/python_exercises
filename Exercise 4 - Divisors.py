# 1. Take a number DONE
# 2. Print out a list of all the divisors of that number
#       For i in range that is less than _num_
#           If number % i is 0
#                append to x
#       Print the list
        

num = int(input("Enter num: "))
x = []

for i in range(1,num):
    if num % i == 0:
        x.append(i)

print(x)


