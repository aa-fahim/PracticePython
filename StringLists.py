## String List

# Asks for a word and then checks if it is a palidrome. 


wrd = input("Please enter a word:\n")
rvs = wrd[::-1]
print(rvs)
print(wrd)

if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

            