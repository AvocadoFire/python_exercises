# Exercise from www.pythonpractice.org
#
# Echo back some words in reverse order

def getstring():
    return input("Type a few words: ")

# Convert the string into a list and reverse it
def split(s):
    a = s.split()
    b = a[::-1]
    return b

# Join the list with spaces so it prints nicely
def join(reverse):
    a = " ".join(reverse)
    return a

s = getstring()
reverse = split(s)
joined = join(reverse)
print ("Original String:\n",s,"\n")
print ("Reversed List:\n",reverse,"\n")
print ("Joined string:\n",joined)








    
