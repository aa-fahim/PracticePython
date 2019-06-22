## Asks for a list from user then outputs elements from the list which are less 
## than 5. Second part of program asks for a number from user to compare list
## with then prints a new line with elements less than that number. 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

for element in a:
    if (element < 5):
        print("{}\n".format(element))
        new_list.append(element)

print(new_list)

check = int(input('Enter a number to see which elements in list are less than:\n'))
another_list = []

for element in a:
    if (element < check):
        another_list.append(element)

print(another_list)