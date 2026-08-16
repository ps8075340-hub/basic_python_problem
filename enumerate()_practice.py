# Practice program on enumerate functions.

fruits = ["Apple", "Banana", "Mango\n"]
for i, fruit in enumerate(fruits):
    print(i, fruit) # Practice 1
    
names = ["Rahul", "Prashant", "Anay\n"]
for i, name in enumerate(names, start = 1):
    print(i, name) # Practice 2
    
nums = [10, 15, 20, 25, 30, 35]
for i, num in enumerate(nums):
    if num % 2 == 0:
        print(i, num) # Practice 3