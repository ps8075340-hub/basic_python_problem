# Practice programs on enumerate functions.

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

numbers = [5, 12, 7, 20, 15, 30, 9, 40]
for i, num in enumerate(numbers, start = 0):
    if num % 2 == 0 and i % 2 != 0:
        print(i,num) # Practice 4

students = ["Rahul", "Prashant", "Anay", "Aman", "Rohit", "Neha"]
marks = [45, 78, 32, 91, 67, 85]
for i, mark in enumerate(marks, start=1):
    if mark >= 60:
        print(i, students[i - 1], mark) # Practice 5

students = ["Rahul", "Prashant", "Anay", "Aman", "Rohit", "Neha"]
marks = [45, 78, 32, 91, 67, 85]
for i, mark in enumerate(marks, start = 1):
    if mark >= 80:
        print("position:", i, students[i - 1], mark) # Practice 6

names = ["A", "B", "C", "D", "E"]
for i, name in enumerate(names[::-1]):
    reversed_position = len(name) - i
    print(i, name) # Practice 7

data = [
    ["Aman", 78, 82],
    ["Rahul", 91, 88],
    ["Neha", 67, 95],
    ["Rohit", 85, 79]
]
for i, student in enumerate(data,  start = 1):
    name = student[0]
    mark_1 = student[1]
    mark_2 = student[2]
    
    average_marks = (mark_1 + mark_2)/ 2
    
    if average_marks >= 85:
        print(i,name, average_marks) # Practice 8