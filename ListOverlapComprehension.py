## List Overlap using Comprehension

# First part involves testing lists a and b, placing their common elements into 
# a new list then printing this new list. Second part involves generating two 
# random sets then testing and printing their common elements without duplicates.


import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list_common = []
list_common = [i for i in set(a) for j in set(b) if i==j]
print(list_common)

list_A = random.sample(range(100), 5)
list_B = random.sample(range(100), 10)

list_overlap = []
list_overlap = [i for i in set(list_A) for j in set(list_B) if i==j]
print(list_overlap)
