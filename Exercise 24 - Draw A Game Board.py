# Exercise 24 - Draw a Game Board from www.pythonpractice.org

def choose_board():
    return int(input("Board Size: "))
    

def draw_board(size):
    for i in range(size):
        print ("---" * int(size))
        print ("|  " * int(size+1))
        print ("---" * int(size))
  
if __name__=="__main__":
    size = choose_board()
    draw_board(size)
