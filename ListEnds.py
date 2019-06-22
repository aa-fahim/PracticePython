## List Ends

# Takes first and last element of input list a and places into new list and 
# prints it.

def list_ends(a):
    a = [5, 10, 15 ,20 ,25]
    new_list = [a[0], a[len(a)-1]]
    print(new_list)