# Program to accept marks of 5 subjects. 

total = 0
count = 1

while count <= 5:
    sub = float(input(f'Enter marks of subject {count} : '))
    total += sub
    count += 1

# Total and Average marks
avg_marks = total / 5

if avg_marks >= 40:
    print('RESULT = PASS')
else:
    print('RESULT = FAIL')

print('Total marks = ', total)
print('Average marks = ', avg_marks)