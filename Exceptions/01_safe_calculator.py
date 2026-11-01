# Remember the calculator from Day 03? Now it can't be broken. get_number() keeps asking until it gets a number, and try / except catches dividing by zero.

# Your job:
# 1. add % (remainder) and ** (power)
# 2. put it all in a while loop and ask
#    "Again? (y/n)" at the end

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please type a number.")


print("=== Safe Calculator ===")

while True:
    a = get_number("First number: ")
    op = input("Choose + - * / % ** : ")
    b = get_number("Second number: ")

    try:
        if op == "+":
            print("Answer:", a + b)
        elif op == "-":
            print("Answer:", a - b)
        elif op == "*":
            print("Answer:", a * b)
        elif op == "/":
            print("Answer:", a / b)
        elif op == "%":
            print("Answer:", a % b)
        elif op == "**":
            print("Answer:", a ** b)
        else:
            print("Unknown sign:", op)

    except ZeroDivisionError:
        print("You can't divide by zero!")

    again = input("Again? (y/n) ").lower()
    if again != "y":
        print("Goodbye!")
        break


# output:

# === Safe Calculator ===
# First number: ten
# Please type a number.
# First number: 10
# Choose + - * / % ** : /
# Second number: 0
# You can't divide by zero!
# Again? (y/n) y

# First number: 5
# Choose + - * / % ** : **
# Second number: 3
# Answer: 125.0
# Again? (y/n) n
# Goodbye!