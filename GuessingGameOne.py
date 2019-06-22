## Guessing Game

# Program will generate a random number between 1 and 9. User must guess a 
# a number within that range, and will be told if their guess is correct
# too low, or too high. In the end, it will tell you how many tries it took.
# User can type exit to stop playing.  

import random

a = random.randint(1, 9)
count = 0

while (True):
    
    inp = input('Guess a number from 1 to 9:\n')

    if inp.lower() == 'exit':
        break
    elif int(inp) < a:
        print('You guessed too low!')
        count += 1
    elif int(inp) > a:
        print('You guessed too high!')
        count += 1
    elif int(inp) == a:
        print('You guessed correctly!')
        count += 1
        print('The number was {} and it took you {} tries'.format(a, count))
        break
