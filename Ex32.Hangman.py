## Hangman

# Hangman game, you got 6 tries. Will ask if you want to keep playing.

import random

def pick_word():
    
    lines = []

    with open('sowpods.txt', 'r') as f:
        lines = f.read()
    
    lines = lines.split('\n')
        
    return random.choice(lines)
    
    
def check(guess, word, empty_word):
    
    list1 = []
    count = 0
    for i in word:
        if i == guess:
            list1.append(count)
        count += 2
    
    list2 = list(empty_word)
    for i in list1:
        list2[i] = guess
    
    str1 = ''.join(list2)
    print(str1)
    return str1


def full_check(empty_word):
    
    if '_' not in empty_word:
        print('You guessed the word correctly!')
        full_word = True
    else:
        full_word = False
    return full_word


def display_body(count):
    
    if count == 0:
        print('|----------|')
        print('|')
        print('|')
        print('|')
        print('--')
    elif count == 1:
        print('|----------|')
        print('|          O')
        print('|')
        print('|')
        print('--')
    elif count == 2:
        print('|----------|')
        print('|          O')
        print('|          |')
        print('|')
        print('--')
    elif count == 3:
        print('|----------|')
        print('|          O')
        print('|         /|')
        print('|')
        print('--')
    elif count == 4:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|')
        print('--')
    elif count == 5:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|         /')
        print('--')
    elif count == 6:
        print('|----------|')
        print('|          O')
        print('|         /|\\')
        print('|         /\\')
        print('--')      


def start_game():
    word = pick_word()
    print(word)
    guessed_letters = ''
    full_word = False
    error_count = 0
    
    print('Welcome to Hangman!')
    empty_word = len(word) * '_ '
    print(empty_word + '\n')
    display_body(error_count)
        
    while(full_word == False):
        while(True):
            inp = input('Guess your letter:')
            guess = inp.upper()
            if guess not in guessed_letters:
                break
            else:
                print("You've already guessed this letter!")
        
        guessed_letters += guess
        
        if guess not in word:
            print('Incorrect! The letter {} is not in the word'.format(guess))
            error_count += 1
            display_body(error_count)
            if error_count > 5:
                print("You've guess incorrectly too many times! Game is done.")
                break
        else:  
            empty_word = check(guess, word, empty_word)
            full_word = full_check(empty_word)
            
            
if __name__ == '__main__':
    
    inp = 'yes'
    
    while inp.lower() == 'yes':
        start_game()
        inp = input('Do you wish to play another game?')
