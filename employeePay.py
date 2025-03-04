# Author: Meghan Carron
# Date: 2/16/2025
# Program: lightyear.py

hourly_wage = float(input("What is the hourly wage? "))
regular_hours = int(input("How many regular hours worked? "))
overtime_hours = int(input("How many overtime hours worked? "))
overtime_pay = overtime_hours * (hourly_wage*1.5)
total_weekly = hourly_wage * regular_hours
print("The total weekly pay is", total_weekly)
