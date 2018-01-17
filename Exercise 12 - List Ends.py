# Exercise from www.pythonpractice.org
#
# 1. Create a random list
# 2. Make a new list of only the first and last numbers

import random

# Create list
a = random.sample(range(50),10)
print (a)
b = []

# Append first and last letters into a new list
def new_list(a):
    b.append(a[0])
    b.append(a[-1])

# Call function and print result :)
new_list(a) 
print (b)
