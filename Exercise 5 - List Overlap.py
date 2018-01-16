# 1. Feed in two lists of different sizes - OK
# 2. Return a list populated by common elements of the two lists - OK
# 3a. Randomly generate two lists to test this
# 3b. Write this is one line of Python 
        

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a:
    if i in b:
        c.append(i)

print(c, "\nw00t")
        
        
        



