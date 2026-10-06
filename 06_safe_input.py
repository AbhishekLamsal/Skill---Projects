# int(input()) crashes when the user types words. get_number() keeps asking until it gets real digits, then returns an int. Use it in every program from now on!
# Your job:
# 1. only accept ages from 1 to 120
# 2. use get_number() in the Day 09 calculator

def get_number(question):
    while True:
        answer = input(question).strip()

        if not answer.isdigit():
            print("Please type a number only")
            continue

        age = int(answer)

        if 1 <= age <= 120:
            return age

        print("Age must be between 1 and 120")

age = get_number("Your age: ")
print(f"Next year you will be {age + 1}")