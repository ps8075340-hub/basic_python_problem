#Program to display a menu for calculating area of a circle or perimeter of a circle.

import math

print('\nEnter 1 for area of circle')
print('\nEnter 2 for perimeter of circle')

choice = int (input ('\nChoose a number 1 or 2 : '))

radius = float (input ('\nEnter radius of a circle : '))

if choice == 1:
    area = math.pi * radius**2
    print(area,'m² is area of circle.')

elif choice == 2:
    perimeter = 2 * math.pi * radius
    print(perimeter,'m is perimeter of circle.')
    
else:
    print('Invalid Choice, Please enter 1 or 2 only')