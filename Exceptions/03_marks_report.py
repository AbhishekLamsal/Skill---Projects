# add_mark() uses raise when a mark is not between 0 and 100. average() returns 0 for an empty list instead of crashing with ZeroDivisionError.

# Your job
# 1. print Pass if average >= 40, else Fail
# 2. print max() and min() of marks. What happens
#    if the list is empty? Catch that error too!


def average(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0


def add_mark(marks, text):
    mark = int(text)

    if mark < 0 or mark > 100:
        raise ValueError("Mark must be 0 to 100")

    marks.append(mark)


marks = []

print("Type marks one by one. Type q to finish.")

while True:
    text = input("Mark: ")

    if text == "q":
        break

    try:
        add_mark(marks, text)
    except ValueError as e:
        print("Skipped:", e)

avg = average(marks)

print("Marks:", marks)
print("Average:", round(avg, 1))

if avg >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

try:
    print("Highest mark:", max(marks))
    print("Lowest mark:", min(marks))
except ValueError:
    print("No marks entered, so there is no highest or lowest mark.")


# output:


# example 1:

# Type marks one by one. Type q to finish.
# Mark: 80
# Mark: abc
# Skipped: invalid literal for int() with base 10: 'abc'
# Mark: 150
# Skipped: Mark must be 0 to 100
# Mark: 70
# Mark: q

# Marks: [80, 70]
# Average: 75.0
# Result: Pass
# Highest mark: 80
# Lowest mark: 70

# example 2:

# Type marks one by one. Type q to finish.
# Mark: q

# Marks: []
# Average: 0
# Result: Fail
# No marks entered, so there is no highest or lowest mark.