import math

radius = int (input("Please enter the radius:"))
height = int (input("Please enter the height:"))

radiusSquared = radius**2
volume = math.pi * radiusSquared * height
print("Your Circle Volume is ", volume)

