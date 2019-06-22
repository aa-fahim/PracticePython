## Guessing Game Two

# Think of a number between 0-100 and let the program try to guess your
# your number. Involves binary searching and will tell you how many tries
# it took.

if __name__ == "__main__":
    
    a = 50
    count = 1
    max = 100
    min = 0
    while(True):
        guess = input('Is your number {}? Enter higher, lower, or yes:\n'.format(a))
        
        if guess.lower() == 'yes':
            print('Nice, success! It took {} tries'.format(count))
            break
        else:
            if guess == 'higher':
                min = a + 1
                a = (max + min)//2
            elif guess == 'lower':
                max = a - 1
                a = (max + min)//2
            count += 1
        
    
    