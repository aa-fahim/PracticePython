## This program will ask the user to input their name and age. It will return
## a messsage stating what year they will turn 100 years old. 

from datetime import datetime

current_date = datetime.now()
current_year = current_date.year

name = input('Enter your name:')
age = int(input('Enter your age:'))
times = int(input('How many times do you want the line to be printed?\n'))

yr_at_100 = current_year + (100 - age)

a = 0
while (a < times):
    print('Hello {}, the year you will turn 100 is {}'.format(name, yr_at_100))
    a += 1

## print('Hello ' ,name, ', the year you will turn 100 is' ,yr_at_100)
## print('Hello ' +name+ ', the year you will turn 100 is' ,yr_at_100)
## print('Hello %s, the year you will turn 100 is %d' %(name, yr_at_100))
