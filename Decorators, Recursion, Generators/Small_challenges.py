# 01 Write a decorator @twice that runs the function two times

def twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@twice
def hello():
    print("Hello!")


hello()

# output

# Hello!
# Hello!

# 02 Write a decorator @smile that adds " :)" to the end of any text the function returns

def smile(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + " :)"
    return wrapper


@smile
def greet():
    return "Good morning"


print(greet())

# output

# Good morning :)

# 03 Write a recursive stars(n) that prints n stars, then n - 1, down to 1

def stars(n):
    if n <= 0:
        return

    print("*" * n)
    stars(n - 1)


stars(5)

# output

# *****
# ****
# ***
# **
# *

# 04 Write a recursive is_palindrome(word). (Hint: compare word[0] and word[-1], then word[1:-1])

def is_palindrome(word):
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:-1])


print(is_palindrome("radar"))
print(is_palindrome("python"))

# output

# True
# False
# 05 Write a generator table(n) that yields "5 x 1 = 5" up to "5 x 10 = 50"

def table(n):
    for i in range(1, 11):
        yield f"{n} x {i} = {n * i}"


for line in table(5):
    print(line)

# output
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# 06 Use sum() with a one-line generator to add the squares of 1 to 10

total = sum(n * n for n in range(1, 11))

print(f"Sum of squares: {total}")

# output

# Sum of squares: 385