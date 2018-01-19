# Exercise 22 - Read from file from www.pythonpractice.org
# from nameslist.txt, count how many of each name there are

def read():
    counter_dict = {}
    with open('nameslist.txt') as f:
        # Load the first line
        line = f.readline()
        # While there is a line
        while line:
            # Strip the line where whitespace begins -->
            line = line.strip()
            # If that line is already in the dictionary, add 1
            if line in counter_dict:
                counter_dict[line] += 1
            # If that line is not already in the dictionary, it's value is 1
            else:
                counter_dict[line] = 1
            # Move to the next line
            line = f.readline()
            
    print(counter_dict)

if __name__=="__main__":
    read()
