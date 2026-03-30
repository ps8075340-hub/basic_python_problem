x = int(input('Enter a Number : '))
y = int(input('Enter a Number : '))
z = int(input('Enter a Number : '))

# Sum1: sum of all numbers
sum1 = x + y + z

# Sum2: sum of non-duplicate numbers
sum2 = 0

if x != y and x != z:
    sum2 += x

if y != x and y != z:
    sum2 += y

if z != x and z != y:
    sum2 += z

print("Sum1 =", sum1)
print("Sum2 =", sum2)
