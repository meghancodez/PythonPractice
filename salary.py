# Author: Meghan Carron
# Date: 3/1/2025
# Program: salary.py

starting_salary = int(input("Enter the starting salary: "))
percent_increase = float(input("Enter the percent increase: "))
numYears = int(input("Enter the number of years in the schedule: "))

#calculate salary based on percent increase and number of years
salary = (starting_salary + (starting_salary * percent_increase)) * numYears

# Display the header
print("Year" + " " * 3 + "Salary")

# Initialize variables
year = 1
salary = starting_salary

# Calculate and display the salary for each year using a while loop
while year <= numYears:
    print(str(year) + " " * 6 + str(salary))
    salary = salary * (1 + percent_increase)
    year = year + 1