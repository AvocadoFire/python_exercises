# Exercise 20 - Element Search from www.pythonpractice.org

# Implement a binary search function in place of the previous one. 

ordered_list = [1, 2, 5, 7, 9, 11, 15, 19, 20, 21, 40, 50]

# Straight Search
def straightsearch(ordered_list,x):
    if x in ordered_list:
        return True
    else:
        return False

# Binary Search
def binarysearch(ordered_list,low,high,x):
    if high >= low:
        mid = int(low + (high - low) / 2)
        if ordered_list[mid] == x:
            print("Found!")
            return True
        elif ordered_list[mid] > x:
            print("Moving down...")
            return binarysearch(ordered_list,low,mid-1,x)
        elif ordered_list[mid] < x:
            print("Moving up...")
            return binarysearch(ordered_list,mid+1,high,x)
    print("Value not found")
    
if __name__=="__main__":

    print("Check 1: ")
    check = binarysearch(ordered_list,0,11,1)
    print("Check 2: ")
    check = binarysearch(ordered_list,0,11,5)
    print("Check 3: ")
    check = binarysearch(ordered_list,0,11,10)
    print("Check 4: ")
    check = binarysearch(ordered_list,0,11,15)
