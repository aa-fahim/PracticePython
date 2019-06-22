## Guess Letters

# The word is EVAPORATE, will ask the user for a letter. If the letter exists
# will update the hidden word showing the corectly guessed letters. If letter
# is duplicate, will ask for a different letter. 

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

if __name__ == '__main__':
    word = 'EVAPORATE'
    guessed_letters = ''
    full_word = False
    
    print('Welcome to Hangman!')
    empty_word = len(word) * '_ '
    print(empty_word)
        
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
        else:  
            empty_word = check(guess, word, empty_word)
            full_word = full_check(empty_word)
        