#Program that reads two numbers and an arithmetic operator and display the computed results (use if-elif).

num_1 = float (input ('Enter first number : '))
num_2 = float (input ('Enter second number : '))

operator = (input ('Enter a oreator (+, -, *, /, %) : '))


#Add
if operator == '+':
    print('Addition of first and second number : ' ,num_1 + num_2)
   
# Sub 
elif operator == '-':
    print('Subtraction of first and second number : ', num_1 - num_2)

#Multiply
elif operator == '*':
    print('Multiplication of first and second number : ', num_1 * num_2)  
  
#Divide 
elif operator == '/':
    if num_2 != 0:
        print('Division of first and second number : ',num_1 / num_2) 
    else:
        print('Error : Division by zero is not allowed.')
    
elif operator == '%':
    if num_2 != 0:
        print('Remainder of first and second number : ', num_1 % num_2)
    else:
        print('Error : Division by zero is not allowed.')
    
else:
    print('Invalid Operator, Please choose only(+,  *, -, %, /).')