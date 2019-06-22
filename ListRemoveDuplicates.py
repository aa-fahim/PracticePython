## List Remove Duplicates

import random
a = [1, 1, 1, 2, 2, 3, 4, 4]

# Takes list a and creates and prints new list without duplicates in a.
# Uses for loop and if statement.
def remove_duplicates(a):
    new_list = []
    
    for i in range(len(a)):
        if a[i] not in new_list:
            new_list.append(a[i])
            
    print(new_list)

# Takes list a and creates and prints new list without duplicates in a.
# Uses set function.
def remove_duplicates_using_sets(a):
    new_list = set(a)
    new_list = list(new_list)
    print(new_list)
    
# Generates two random lists and finds their common elements without duplicates.
# Prints the two generated lists and the final common list.
# Uses set function. 
def set_of_two_random_generated_list():

    random_list_1 = random.sample(range(20), 20)
    random_list_2 = random.sample(range(20), 10)
    print(random_list_1)
    print(random_list_2)
    
    new_list = [i for i in set(random_list_1) for j in set(random_list_2) if i==j]
    
    print(new_list)