#1 Task Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = reduce(lambda x, y: x * y, numbers)
print("Result of multiplying all numbers:", result)

#2 Task Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
input_string = input("Enter a string: ")
upper_count = sum(1 for char in input_string if char.isupper())
lower_count = sum(1 for char in input_string if char.islower())
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

#3 Task Write a Python program with builtin function that checks whether a passed string is palindrome or not.
input_string = input("Enter a string: ")
if input_string == input_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4 Task Write a Python program that invoke square root function after specific milliseconds
import time
import math
number = float(input("Enter a number to find its square root: "))
milliseconds = int(input("Enter the number of milliseconds to wait before calculating the square root: "))
time.sleep(milliseconds / 1000)
result = math.sqrt(number)
print(f"The square root of {number} is: {result}")

#5 Task Write a Python program with builtin function that returns True if all elements of the tuple are true.
user_input = input("Enter elements of the tuple separated by spaces: ")
user_tuple = tuple(map(str, user_input.split()))
result = all(user_tuple)
print(result)