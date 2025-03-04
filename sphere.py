#Author: Meghan Carron
#Date: 2/9/2025
#Program: sphere.py

#prompt user for input
radius = float(input("What is the radius? "))

#calculate the diameter of the sphere
diameter = (2 * radius)

#calculate the circumference of the sphere
circumference = diameter * 3.14

#calculate the surface area of the sphere
surface_area = (4 * 3.14) * (radius*radius)

#calculate the volume of the sphere
volume = (4/3 * 3.14) * (radius*radius*radius)

#display the results
print("The volume of the sphere is ", volume)
print("The diameter of the sphere is ", diameter)
print("The surface area of the sphere is ", surface_area)
print("The circumference of the sphere is ", circumference)