## Check Tic Tac Toe

# Program will check if there is player who won in a tic tac toe game. Where
# 1 represents player 1, 2 represents player 2, and 0 means no player has 
# selected that location. Program checks if player 1 or 2 has 3 in a row
# horizontally, vertically or diagonally. If no player has 3 in a row, then
# winner will be no one. Main function tests 5 examples.

    
def check_tic_tac_toe(a):
    
    winner = 0
    if a[0][0] == a[1][1] == a[2][2]:
        winner = a[0][0]
    elif a[2][0] == a[1][1] == a[0][2]:
        winner = a[2][0]
    else:
        for i in range(3):
            if a[i][0] == a[i][1] == a[i][2]:
                winner = a[i][0]
            elif a[0][i] == a[1][i] == a[2][i]:
                winner = a[0][i]
    
    if winner == 0:
        print('There is no winner!')
    else:
        print('Winner is {}!'.format(winner))

if __name__ == "__main__":
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
    
    check_tic_tac_toe(winner_is_2)
    check_tic_tac_toe(winner_is_1)
    check_tic_tac_toe(winner_is_also_1)
    check_tic_tac_toe(no_winner)
    check_tic_tac_toe(also_no_winner)