## Takes two arrays and finds the commone elements placing them in new array 
## without duplicates. Prints new array. Generates two random arrays and repeats
## the same process. WIll display two randomly generated arrays and another array
## showing their common elements. 

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list = []

for i in a:
    for j in b:
        if i == j and i not in list:
            list.append(i)
print(list)

random_list_1 = random.sample(range(20), 20)
random_list_2 = random.sample(range(20), 10)
print(random_list_1)
print(random_list_2)

new_list = []

for a in random_list_1:
    for b in random_list_2:
        if a == b and a not in new_list:
            new_list.append(a)
print(new_list)
