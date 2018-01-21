# Exercise 26 - Check Tic Tac Toe from www.pythonpractice.org

# Test Cases
winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

def check_win(board):
    for player in range(1,3):
        # Horizontal
        if (
            (board[0][0] == player and board[0][1] == player and board[0][2] == player)
        or (board[1][0] == player and board[1][1] == player and board[1][2] == player)
        or (board[2][0] == player and board[2][1] == player and board[2][2] == player)
        # Vertical
        or (board[0][0] == player and board[1][0] == player and board[2][0] == player)
        or (board[0][1] == player and board[1][1] == player and board[2][1] == player)
        or (board[0][2] == player and board[1][2] == player and board[2][2] == player)
        # Diagonal
        or (board[0][0] == player and board[1][1] == player and board[2][2] == player)
        or (board[0][2] == player and board[1][1] == player and board[2][0] == player)
            ):
            print("Player %s Wins!" % player)
            return
    print("Nobody wins")
    return
            

if __name__=="__main__":
    check_win(winner_is_also_1)
    check_win(no_winner)
    check_win(winner_is_1)
    check_win(winner_is_2)
    check_win(also_no_winner)
    
    
    

