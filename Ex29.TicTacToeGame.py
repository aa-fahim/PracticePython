## Tic Tac Toe Game

# Fills the board with X if player one or O if player two. Will check if input 
# is valid meaning if there is already a mark where the player is requesting
# to put their mark. Once all the spots on the board are filled, the game
# will end.

# More specifics. Player one with 'X' will have the first move in the very
# first game, then it will alternate between player 2 and player 1 having
# the first move. Program will tell you if there was a draw or which player won.
# It will also record how many game were played, and how many each player won
# or how many draws there have been.

def play_game(board, count):

    draw_board(board)
    while(full_board(board) == False):
        game_done, player = check_tic_tac_toe(board)
        if game_done == True:
            return player
            break

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
                        '(row:1-3, col:1-3)):'.format(player))
            location = inp.split(',')
            board, valid = draw_tic(board, location, mark)
    
    if full_board(board) == True:
        player = 0
        return player

def full_board(board):
    full_board = True
    
    for i in range(len(board[0])):
        for j in range(len(board[1])):
            if board[i][j] == 0:
                #print('true')
                full_board = False 
    return full_board


def draw_tic(board, inp, mark):
    if board[int(inp[0]) - 1][int(inp[1]) - 1] == 0:
        board[int(inp[0]) - 1][int(inp[1]) - 1] = mark
        draw_board(board)
        valid = True
    else:
        print('The location you selected has already been taken, please '
              'enter another location.')
        draw_board(board)
        valid = False
    return board, valid


def check_tic_tac_toe(a):
    winner = 0
    game_done = False
    player = 0
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
    
    if winner == 'X':
        player = 1
    elif winner == 'O':
        player = 2
        
    if winner != 0:
        game_done = True
        print('Winner is Player {}!'.format(player))
    return game_done, player

def draw_board(board):
    dashes = ' --- --- ---'
    line = '|'
    print(dashes)
    print(line,board[0][0],line,board[0][1],line,board[0][2],line)
    print(dashes)
    print(line, board[1][0], line, board[1][1], line, board[1][2], line)
    print(dashes)
    print(line, board[2][0], line, board[2][1], line, board[2][2], line)
    print(dashes)

if __name__ == '__main__':
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    finished = 'yes'
    player_1_count = 0
    player_2_count = 0
    draw_count = 0
    count = 0
    
    while finished.lower() == 'yes':
        player_count = play_game(board, count)
        count += 1
        if player_count == 0:
            draw_count += 1
        elif player_count == 1:
            player_1_count += 1
        elif player_count == 2:
            player_2_count += 1
        if player_count == 0:
            print('All locations on board are filled, there is no winner.')
        if count > 1:
            print('{} games were played'.format(count))
        else:
            print('1 game was played')
        
        print('Player 1 has won {} games, player 2 has won {} games and there '
              'have been {} draws'.format(player_1_count, player_2_count, 
                         draw_count))
        
        finished = input('Do you want to play another game?')
        if finished.lower() == 'yes':
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
    