# Author: Meghan Carron
# Date: 2/16/2025
# Program: lightyear.py

import math

#calculate lightspeed/get the result of (3) x (10 to the power of 8)
base = 10
exponent = 8
lightspeed = 3*(pow(base, exponent))

#calculate lightyear/figure out how many seconds are in a year
lightyear = 60 * 60 * 24 * 365

#get # years from user
numYears = int(input("Enter a number of years: "))

#calculate speed of light depending on num years
distance = lightspeed * lightyear * numYears

#display distance traveled
print("Light traveled", distance, "meters in", numYears, "years.")