# Program to find lowest and second lowest integer from 10 integers.

lowest = float('inf')
second_lowest = float('inf')

for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))

    if num < lowest:
        second_lowest = lowest
        lowest = num
    elif num < second_lowest and num != lowest:
        second_lowest = num

print("Lowest:", lowest)

if second_lowest == float('inf'):
    print("Second lowest not found (all numbers may be same)")
else:
    print("Second Lowest:", second_lowest)  