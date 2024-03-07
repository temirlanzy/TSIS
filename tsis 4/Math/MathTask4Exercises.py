#Exercise 1(Task 4) Write a Python program to convert degree to radian. 
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian: {:.6f}".format(radian))

#Exercise 2(Task 4) Write a Python program to calculate the area of a trapezoid.
height = float(input("Height: "))
base_first = float(input("Base, first value: "))
base_second = float(input("Base, second value: "))
area = ((base_first + base_second) / 2) * height
print("Expected Output:", area)

#Exercise 3(Task 4) Write a Python program to calculate the area of regular polygon. 
from math import tan, pi
n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
area = (n_sides * (side_length ** 2)) / (4 * tan(pi / n_sides))
print("The area of the polygon is:", area)

#Exercise 4(Task 4) Write a Python program to calculate the area of 1 a-parallelogram.
base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base_length * height
print("Expected Output:", area)