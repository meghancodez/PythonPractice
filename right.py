#Author: Meghan Carron
#Date: 2/24/2025
#Program: right.py

side1 = int(input("Enter length of side 1: "))
side2 = int(input("Enter length of side 2: "))
side3 = int(input("Enter length of side 3: "))

if (side1 ** 2) == (side2 ** 2) == (side3 ** 2):
    print("This is a NOT a right triangle.")
elif (side1 ** 2) == (side2 ** 2) + (side3 ** 2):
    print("This is a right triangle.")
elif (side2 ** 2) == (side1 ** 2) + (side3 ** 2):
    print("This is a right triangle.")
elif (side3 ** 2) == (side1 ** 2) + (side2 ** 2):
    print("This is a right triangle.")
else:
    print("This is NOT a right triangle.")