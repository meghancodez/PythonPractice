#Author: Meghan Carron
#Date: 2/16/2025
#Program: momentum2.py

mass = int(input("Enter the object's mass (in kg): "))
velocity = int(input("Enter the object's velocity (in m/s): "))
momentum = mass * velocity
kinetic_energy=(1/2)*(momentum)*(velocity*velocity)
print("The momentum is", momentum)
print("The kinetic energy is", kinetic_energy)