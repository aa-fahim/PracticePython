## Password Generator

# Asks user if they want a strong or weak randomly generated password. If they
# chose weak then will output a password thats takes a word from two different 
# lists and combines them. Choosing strong will output a password of length 8 
# using Capatial and lowercase letters, numbers and symbols.

import random

inp = input('How strong do you want your password: weak or strong?\n')

if (inp.lower() == 'strong'):
    
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p =  "".join(random.sample(s,passlen ))
    print(p)
    
elif(inp.lower() == 'weak'):
    list_A = ['Chicken', 'Beef', 'Fish', 'Shrimp', 'Steak']
    list_B = ['Rice', 'Noodles', 'Alone', 'Bread', 'More_meat']
    password="".join([list_A[random.randint(0, 4)], 
                       list_B[random.randint(0,4)]])
    print(password)