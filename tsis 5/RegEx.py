with open(r'C:\Users\ADMIN\Рабочий стол\lab5\reg.txt') as file:
    reg=file.read()
import re

#1 Task. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
pattern = re.compile(r'ab*')
def match_string(text):
    return bool(pattern.fullmatch(text))
text = input("Enter a string: ")
print(match_string(text))

#2 Task. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
pattern = re.compile(r'ab{2,3}')
def match_string(text):
    return bool(pattern.fullmatch(text))
text = input("Enter a string: ")
print(match_string(text))

#3 Task. Write a Python program to find sequences of lowercase letters joined with an underscore.
import re
pattern = re.compile(r'[a-z]+_[a-z]+')
def find_sequences(text):
    return pattern.findall(text)
text = input("Enter a string: ")
print(find_sequences(text))

#4 Task. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
pattern = re.compile(r'[A-Z][a-z]+')
def find_sequences(text):
    return pattern.findall(text)
text = input("Enter a string: ")
print(find_sequences(text))

#5 Task. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
pattern = re.compile(r'a.*b$')
def match_string(text):
    return bool(pattern.fullmatch(text))
text = input("Enter a string: ")
print(match_string(text))

#6 Task. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
def replace_chars(text):
    return re.sub(r'[ ,.]', ':', text)
text = input("Enter a string: ")
print(replace_chars(text))

#7 Task. Write a python program to convert snake case string to camel case string.
def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))
text = input("Enter a string in snake_case: ")
print(snake_to_camel(text))

#8 Task. Write a Python program to split a string at uppercase letters.
import re
def split_at_uppercase(text):
    return re.findall('[A-Z][^A-Z]*', text)
text = input("Enter a string: ")
print(split_at_uppercase(text))

#9 Task. Write a Python program to insert spaces between words starting with capital letters.
import re
def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
text = input("Enter a string: ")
print(insert_spaces(text))

#10 Task. Write a Python program to convert a given camel case string to snake case.
import re
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
text = input("Enter a string in CamelCase: ")
print(camel_to_snake(text))