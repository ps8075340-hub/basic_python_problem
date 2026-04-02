# Program: Income Tax Calculator

salary = float(input('Enter your salary: '))

if salary <= 250000:
    print('No Tax')

elif salary <= 500000:
    tax = 0.05 * salary
    print('Tax:', tax)
    print('Salary:', salary)

elif salary <= 1000000:
    tax = 0.10 * salary
    print('Tax:', tax)
    print('Salary:', salary)

else:
    tax = 0.20 * salary
    print('Tax:', tax)
    print('Salary:', salary)