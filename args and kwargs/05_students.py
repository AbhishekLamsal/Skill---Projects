# Every student can have different details, so add_student() uses **info. Each dictionary is added to a list (Day 04), then printed with enumerate().
# Your job:
# 1. print only the students who have a "city"
#    (hint: "city" in s, Day 06)
# 2. print the average age of all students

def add_student(students, **info):
    students.append(info)
    print(f"Added: {info.get('name', 'Unknown')}")


students = []

add_student(students, name="Ram", age=21, city="Pokhara")
add_student(students, name="Sita", age=22)
add_student(students, age=19, city="Butwal")

print("\nAll Students:")
for num, s in enumerate(students, start=1):
    print(f"{num}. {s}")


# Task 1: Print only students who have a city
print("\nStudents with a city:")
for s in students:
    if "city" in s:
        print(s)


# Task 2: Print the average age of all students
ages = []

for s in students:
    if "age" in s:
        ages.append(s["age"])

average_age = round(sum(ages) / len(ages), 2)

print(f"\nAverage age: {average_age}")

'''
    output
Added: Ram
Added: Sita
Added: Unknown

All Students:
1. {'name': 'Ram', 'age': 21, 'city': 'Pokhara'}
2. {'name': 'Sita', 'age': 22}
3. {'age': 19, 'city': 'Butwal'}

Students with a city:
{'name': 'Ram', 'age': 21, 'city': 'Pokhara'}
{'age': 19, 'city': 'Butwal'}

Average age: 20.67
   '''