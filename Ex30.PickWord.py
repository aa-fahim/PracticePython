## Pick Word

# Picks a random word from the sowpods.txt file which contains a list of 
# the official words used in Scrabble game.

import random

lines = []

with open('sowpods.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')
    
print('Random word from sowpods list: {}'.format(random.choice(lines)))
