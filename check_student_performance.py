# Program to check the improvement of a student.

inc = 0
dec = 0
count = 2
previous = float (input ('Marks in Test 1: '))

while count <= 5:
    current = float (input (f'Marks in Test {count}: '))
    count += 1

# Compare     
    if current > previous:
        inc += 1
    elif current < previous:
        dec += 1
        
        previous = current

# decision        
if inc == 4:
        print('Performance improving')
elif dec == 4:
        print('Performance declining')
else:
        print('Performance incosistent')