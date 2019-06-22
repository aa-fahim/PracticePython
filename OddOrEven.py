## The programs asks the user to input an integer. The program will then
## determine if the number is odd or even and also if it is a multiple of 4.
## The second part of program will ask for two numbers and then check
## if they are divisble or not. 

number = int(input('Please enter a number:\n'))

a = number % 2
b = number % 4

if (a == 0):
    print('The number {} is even'.format(number))
elif (a == 1):
    print('The number {} is odd'.format(number))
    
if (b == 0):
    print('The number {} is a multiple of 4'.format(number))

num = int(input('Enter another number:\n'))
check = int(input('Enter a number to divide by:\n'))

c = num % check

if (c == 0):
    print('The number {} is divisible by {}'.format(num, check))
elif (c != 0):
    print('The number {} is not divisble by {}'.format(num, check))

