## Max of Three

# Will ask for three numbers and will return the largest of those 3.

def MaxOfThree(a, b, c):
    
    if a > b:
        if a > c:
            max = a
        else:
            max = c
    else:
        if b > c:
            max = b
        else:
            max = c
    
    print(max)