# 01 Write cube = lambda n: ... that gives n × n × n. cube(3) gives 27

cube = lambda n: n * n * n
print(cube(3))

# output 

# 27


# 02 Write a lambda is_adult that gives True if the age is 18 or more

is_adult = lambda age: age >= 18
print(is_adult(20))
print(is_adult(15))

# output 

# True
# False


# 03 Sort ["Ram", "sita", "Hari", "gita"] A to Z, ignoring capitals. (Hint: key=lambda n: n.lower())

names = ["Ram", "sita", "Hari", "gita"]
sorted_names = sorted(names, key=lambda n: n.lower())
print(sorted_names)

# output 

# ['gita', 'Hari', 'Ram', 'sita']


# 04 Use map() to turn [1, 2, 3, 4] into ['1', '2', '3', '4']

numbers = [1, 2, 3, 4]
strings = list(map(lambda n: str(n), numbers))
print(strings)

# output 

# ['1', '2', '3', '4']


# 05 Use filter() to keep the numbers from 1 to 30 that divide by 3. (Hint: range(), Day 08)

numbers = range(1, 31)
div_by_3 = list(filter(lambda n: n % 3 == 0, numbers))
print(div_by_3)

# output 

# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


# 06 Update your Day 10 marks analyzer to find the topper with max(..., key=lambda ...)

students = [
    {"name": "Ram", "marks": 78},
    {"name": "Sita", "marks": 92},
    {"name": "Hari", "marks": 35},
    {"name": "Gita", "marks": 85},
]

topper = max(students, key=lambda s: s["marks"])
print(f"Topper: {topper['name']} ({topper['marks']})")

# output 

# Topper: Sita (92)