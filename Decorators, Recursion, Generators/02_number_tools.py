# Three small recursive functions, each with a base case and a smaller step. n % 10 gives the last digit and n // 10 removes it (Day 03). Fibonacci: each number is the sum of the two before it.

# Your job:
# 1. ask the user for a number with int(input())
# 2. write power(base, n) with recursion
# 3. write count_vowels(word) with recursion
#    (hint: word[0] in "aeiou", then word[1:])


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base, n):
    if n == 0:
        return 1
    return base * power(base, n - 1)


def count_vowels(word):
    if word == "":
        return 0

    first = 1 if word[0].lower() in "aeiou" else 0
    return first + count_vowels(word[1:])


number = int(input("Enter a number: "))

print(f"{number}! = {factorial(number)}")
print(f"Digits of {number} add to {sum_digits(number)}")

print(f"Fibonacci: ", end="")
for i in range(number):
    print(f"{fibonacci(i)}", end=" ")
print()

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base}^{exponent} = {power(base, exponent)}")

word = input("Enter a word: ")
print(f"Vowels in '{word}': {count_vowels(word)}")


# output

# Enter a number: 9
# 9! = 362880
# Digits of 9 add to 9
# Fibonacci: 0 1 1 2 3 5 8 13 21 
# Enter the base: 5
# Enter the exponent: 8
# 5^8 = 390625
# Enter a word: sita
# Vowels in 'sita': 2
