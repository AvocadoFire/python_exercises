# Exercise 27 - Get module Tic Tac Toe from www.pythonpractice.org


def get_move():
    move = list(input("Enter 'Row,Col': "))
    x = int(move[0]) - 1
    y = int(move[2]) - 1
    return x,y

if __name__=="__main__":
    p1x,p1y = get_move()
    print(p1x,p1y)
    p2x,p2y = get_move()
    print(p2x,p2y)

    

