# Ask the user for a string and print whether it is a palindrome or not
#       Get string
#       If the letters starting from the beginning of string are the same as from the end
#           Print string, say it's a palindrome
#       If the string is not a palindrome
#           Print string, say it's not a palindrome
        

string = input("Enter a word: ")

if string[:] == string [::-1]:
    print(string,"<<< This is a palindrome")
else:
    print(string,"<<< This is not a palindrome")

        
        


