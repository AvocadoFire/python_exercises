# Return a list of common values without duplicates.
# Use at least one list comprehension
# Create random lists

import random

# Random list creation: 0 - 100, 15 digit lists
a = random.sample(range(100),15)
b = random.sample(range(100),15)

# Create one list if the numbers are found in each (i.e. if they -= to 0)
c = [i for i in a for j in b if j - i == 00]

# Go througe the reduced, single list and remove duplicates
seen = set()
d = [i for i in c if i not in seen and not seen.add(i)]

# Print results :)  
print(d)
