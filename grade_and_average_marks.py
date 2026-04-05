# Program to accept marks of 5 subjects

total = 0
fail = False

for i in range(1, 6):
    
    
    while True:
            sub = float(input(f'Enter marks of subject {i} : '))
            if 0 <= sub <= 100:
                 break   # valid input → exit loop
                 
            else:
                print("Invalid marks! Enter between 0 and 100.")
    if sub < 33:
        fail = True
    if sub >= 80:
        print('A grade')
    elif sub >= 60:
        print('B grade')
    else:
        print('C grade')
    total += sub

# Total and Average marks
avg_marks = total / 5

if fail:
    print('RESULT = FAIL')
    
elif avg_marks >= 40:
    print('RESULT = PASS')

else:
    print('RESULT = FAIL')
    

print('Total marks = ', total)
print('Average marks = ', avg_marks)