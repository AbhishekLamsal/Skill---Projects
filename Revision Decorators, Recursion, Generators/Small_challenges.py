# 01 Decorator @stars that prints ***** before and after any function

def stars(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper


@stars
def hello():
    print("Hello!")


hello()

# output:

# *****
# Hello!
# *****

# 02 Decorator @twice that runs the function two times

def twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@twice
def greet():
    print("Hi!")


greet()

# output:

# Hi!
# Hi!


# 03 Recursive count_up(n) that prints 1 up to n (hint: call first, then print)

def count_up(n):
    if n == 0:
        return

    count_up(n - 1)
    print(n)


count_up(5)

# output:

# 1
# 2
# 3
# 4
# 5


# 04 Recursive multiply(a, b) using only + (hint: a + multiply(a, b - 1))

def multiply(a, b):
    if b == 0:
        return 0

    return a + multiply(a, b - 1)


print(multiply(4, 3))

# output:

# 12


# 05 Generator evens(limit) that yields 0, 2, 4 ... up to limit

def evens(limit):
    n = 0

    while n <= limit:
        yield n
        n += 2


for num in evens(10):
    print(num)

# output:

# 0
# 2
# 4
# 6
# 8
# 10


# 06 Generator table(n) that yields 5 x 1 = 5 up to 5 x 10 = 50

def table(n):
    for i in range(1, 11):
        yield f"{n} x {i} = {n * i}"


for line in table(5):
    print(line)

# output:

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