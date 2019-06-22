## Draw A Game Board

#

def draw_board(a):
    
    for i in range(a):
        draw_horizontal(a)
        draw_vertical(a)
    draw_horizontal(a)


def draw_horizontal(a):
    print(a*' ---')

def draw_vertical(a):
    print((a+1)*'|   ')
    

if __name__ == "__main__":
    a = input('What size of game board do you want to create? Enter '
              'a number N such that NxN board is created.' )
    draw_board(int(a))