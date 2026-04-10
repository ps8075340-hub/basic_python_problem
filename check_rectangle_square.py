# Program to check rectangle and square.

while True:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))

    if length == breadth:
        print("It is a Square")
    else:
        print("It is a Rectangle")

    choice = input("Check again? (yes/no): ")
    if choice.lower() != "yes":
        break