# Program to find largest number. 
def largest(a, b, c):
    if a > b and a > c:
        print(a, "is the largest number.")
    elif b > a and b > c:
        print(b, "is the largest number.")
    else:
        print(c, "is the largest number.")

largest(3, 4, 9)