## Tic Tac Toe Draw

# Fills the board with X if player one or O if player two. Will check if input 
# is valid meaning if there is already a mark where the player is requesting
# to put their mark. Once all the spots on the board are filled, the game
# will end.

def play_game():
    
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    count = 0
    while(full_board(board) == False):
        print(board)
        
        if count % 2 == 0:
            player = 1
            mark = 'X'
        else:
            player = 2
            mark= 'O'
            
        valid = False
        count += 1
        
        while valid == False:
            inp = input('Player {} choose where to put your x (in the form: '
                        '(1-3, 1-3)):'.format(player))
            location = inp.split(',')
            board, valid = draw_tic(board, location, mark)           
        
def full_board(board):
    full_board = True
    
    for i in range(len(board[0])):
        for j in range(len(board[1])):
            if board[i][j] == 0:
                #print('true')
                full_board = False 
    if full_board == True:
        print('All locations on board are filled, game is finished.')
    return full_board

def draw_tic(board, inp, mark):
    if board[int(inp[0]) - 1][int(inp[1]) - 1] == 0:
        board[int(inp[0]) - 1][int(inp[1]) - 1] = mark
        print(board)
        valid = True
    else:
        print('The location you selected has already been taken, please '
              'enter another location.')
        print(board)
        valid = False
    return board, valid
