## Birthday Dictionaries

#

dictionary = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815'
}


    
print('Welcome to the birthday dictionary. We know the birthdays of:')

for name in dictionary:
    print(name)
    
inp = input("Who's birthday do you want to look up?")
print(dictionary.get(inp, 'No name like this exists in our database'))
