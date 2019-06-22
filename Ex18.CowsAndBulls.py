## Cows and Bulls

# Program will generate random 4-digit number from 0000-9999. User has to guess
# the number. Guessing a digit in the right location will earn one cow where
# guessing a digit in the incorrect location will earn one bull. Guessing
# a digit that is not in any location of the generated number will earn
# nothing. 

# Program does not work properly for guessing duplicate digits.

import random

def play_game(a, count):
    print(a)
    p = input('Please enter a 4-digit number:')
    
    str_a = a
    str_p = [int(d) for d in str(p)]
    
    cow = 0
    bull = 0
    
    for i in range(len(str_a)):
        if str_a[i] == str_p[i]:
            cow += 1
        else:
            for j in range(len(str_p)):
                if str_a[i] == str_p[j]:
                    bull += 1

    if cow < 4:
        print('{} cows, {} bulls'.format(cow, bull))
    else:
        print('You guess the correct number! Answer was {} and it took you \
              {} tries.'.format(a, count))
        
    print(str_a)
    return cow
    
if __name__=="__main__":
    
    a = []
    for i in range(4):
        a.append(random.randint(0,9))

    count = 0
    
    while(True):
        correct = play_game(a, count)
        count += 1
        if correct == 4:
            break
        

    