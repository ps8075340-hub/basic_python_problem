#  Program to test  the divisibility of a number  with another number

num_1 = int (input ('Enter a Number : '))
num_2 = int (input ('Enter a Number : '))

if num_2 == 0:
    print('Division by zero is not allowed.')

elif num_1 % num_2 == 0:
    print('It is divisible.')
    
else:
    print( 'It is  not divisible.')

