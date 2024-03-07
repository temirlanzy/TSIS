def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces


def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


def solve(numheads, numlegs):
    rabbits = (numlegs - (2 * numheads)) / 2
    chickens = numheads - rabbits
    return int(chickens), int(rabbits)


def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]


from itertools import permutations

def string_permutations(input_str):
    return [''.join(p) for p in permutations(input_str)]


def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    return '007' in ''.join(map(str, nums))


def sphere_volume(radius):
    volume = (4 / 3) * 3.14159 * radius**3
    return volume


def unique_elements(input_list):
    return list(dict.fromkeys(input_list))


def is_palindrome(word):
    return word == word[::-1]


def histogram(numbers):
    for num in numbers:
        print('*' * num)


import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    target_number = random.randint(1, 20)
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1

        if guess < target_number:
            print("Your guess is too low.")
        elif guess > target_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break