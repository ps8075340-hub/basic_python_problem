# Program to check equilateral triangle. 

choice = 'y'

while choice == 'y':
    a = int(input('Enter angle 1 : '))
    b = int(input('Enter angle 2 : '))
    c = int(input('Enter angle 3 : '))

    if a == b == c and a + b + c == 180:
        print('It is an Equilateral Triangle.')
    else:
        print('It is not an Equilateral Triangle.')

    choice = input('Do you want to continue(y/n): ')

print('Thank you!')