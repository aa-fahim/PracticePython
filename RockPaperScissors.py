## Simple Rock Paper Scissors game 

print("Hello, welcome to Fahim's Rock Paper Scissors game!")

option = 'yes'

while (option.lower() != 'no'):
    
    player1 = input('Player One choose one: Rock, Paper or Scissors\n')
    while player1.lower() != 'rock' and player1.lower() !='paper' and \
    player1.lower() !='scissors':
        print('Not a valid input')
        player1 = input('Player One choose one: Rock, Paper or Scissors\n')
    
    player2 = input('Player Two choose one: Rock, Paper or Scissors\n')
    while player2.lower() != 'rock' and player2.lower() !='paper' and \
    player2.lower() !='scissors':
        print('Not a valid input')
        player2 = input('Player Two choose one: Rock, Paper or Scissors\n')

    if player1.lower() == 'rock':
        if player2.lower() == 'rock':
            print('Both players chose rock, game is a draw!')
        if player2.lower() == 'scissors':
            print('Rock beats scissors so Player One wins!')
        if player2.lower() == 'paper':
            print('Paper beats rock so Player Two wins!')
            
    if player1.lower() == 'paper':
        if player2.lower() == 'rock':
            print('Paper beats rock so Player One wins!')
        if player2.lower() == 'scissors':
            print('Scissors beats paper so Player Two wins!')
        if player2.lower() == 'paper':
            print('Both players chose paper, game is a draw!')
            
    if player1.lower() == 'scissors':
        if player2.lower() == 'rock':
            print('Rock beats scissors so Player Two wins!')
        if player2.lower() == 'scissors':
            print('Both players chose scissors, game is a draw!')
        if player2.lower() == 'paper':
            print('Scissors beat paper so Player One wins!')
    
    option = input('Would you like to play another game?\n')
    while option.lower() != 'yes' and option.lower() != 'no':
        print('Not a valid input')
        option = input('Would you like to play another game?\n')

