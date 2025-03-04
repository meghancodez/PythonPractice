# Author: Meghan Carron
# Date: 2/9/2025
# Program: Five Star Video Rentals

#initialize constants
NEW_RENTAL = 3.00
OLDIE_RENTAL = 2.00

#request inputs
newOnes = float(input("How many of the NEW videos did the customer rent? "))
oldOnes = float(input("How many of the OLD videos did the customer rent? "))

#compute result
totalCost = (NEW_RENTAL * newOnes) + (OLDIE_RENTAL * oldOnes)

#display total cost
print("The total cost of the customer's rentals is ", totalCost)