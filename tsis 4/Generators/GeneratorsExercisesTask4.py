#Exercise 1 A generator that generates the squares of numbers up to some number N.
def generate_squares(N):
    for i in range(N+1):
        yield i ** 2
N = int(input())
for square in generate_squares(N):
    print(square)

#Exercise 2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i
n = int(input())
print(','.join(map(str, even_numbers(n))))

#Exercise 3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def fun3(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
m = int(input())
d = fun3(m)
for i in d:
    print(i)

#Exercise 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def fun4(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
po = fun4(a, b)
for result in po:
    print(result)

#Exercise 5 Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input("Enter a number to start the countdown: "))
for number in countdown(n):
    print(number)