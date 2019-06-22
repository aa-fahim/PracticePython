## Takes array a and places elements which are even in new array then prints it

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

new_a = [i for i in a if i % 2 == 0]
print(new_a)