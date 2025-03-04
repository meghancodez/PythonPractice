# Author: Meghan Carron
# Date: 3/1/2025
# Program: population.py

numOrgs = int(input("How many organisms (initially)? "))
growth_rate = int(input("Enter rate of growth (real number greater than 0): "))
growth_rate_hours = int(input("How many hours will it take to achieve this rate of growth? "))
numHours = int(input("How long will population grow for? "))

#calculate number of growth periods
growth_periods = numHours / growth_rate_hours

#calculate total population
total_pop = numOrgs * (growth_rate ** growth_periods)

#display total population
print("The total population after", growth_rate_hours, "is", total_pop)