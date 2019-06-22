## Element Search

#

def element_search(a, b):
    
    if b == a[len(a)//2]:
        new_a = [a[len(a)//2]]
        print(new_a)
    elif b > a[len(a)//2]:
        new_a = a[len(a)//2 + 1: len(a)]
        print(new_a)
    elif b < a[len(a)//2]:
        new_a = a[0 : len(a)//2]
        print(new_a)
        
    return new_a
    
    
    
if __name__=="__main__":
    original_a = [1, 2, 7, 7, 7, 7, 9, 10]
    b = 1
    a = original_a

    while (True):
        if (len(a) != 1):
            a = element_search(a, b)
        else:
            if a[0] == b:
                print('The element {} is in the list {}'.format(b, original_a))
            else:
                print('The element {} is not in the list {}'.format(b, original_a))
            break
    