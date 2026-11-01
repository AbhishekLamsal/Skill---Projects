# 01 Class Book with title, author and price. Make 3 books and print each title

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


book1 = Book("Python Basics", "Ram Sharma", 500)
book2 = Book("Learn Django", "Sita Karki", 700)
book3 = Book("Data Science", "Hari Nepal", 900)

print(book1.title)
print(book2.title)
print(book3.title)

# output:

# Python Basics
# Learn Django
# Data Science

# 02 Add a method info() to Book that prints Title by Author: Rs. price

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def info(self):
        print(f"{self.title} by {self.author}: Rs. {self.price}")


book = Book("Python Basics", "Ram Sharma", 500)
book.info()

# output:

# Python Basics by Ram Sharma: Rs. 500

# 03 Class Circle with radius and a method area() that returns 3.14 * r * r

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


c = Circle(5)

print("Radius:", c.radius)
print("Area:", c.area())

# output:

# Radius: 5
# Area: 78.5

# 04 Class Counter with count = 0 and methods increase() and reset()

class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1

    def reset(self):
        self.count = 0


c = Counter()

print(c.count)

c.increase()
c.increase()
c.increase()

print(c.count)

c.reset()

print(c.count)

# output:

# 0
# 3
# 0

# 05 Class Light with is_on = False and a method switch() that turns it on or 

class Light:
    def __init__(self):
        self.is_on = False

    def switch(self):
        self.is_on = not self.is_on

        if self.is_on:
            print("Light is ON")
        else:
            print("Light is OFF")


light = Light()

light.switch()
light.switch()
light.switch()

# output:

# Light is ON
# Light is OFF
# Light is ON

# 06 Class Employee with name, salary and a method give_raise(amount)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount


emp = Employee("Rita", 30000)

print("Name:", emp.name)
print("Salary before raise:", emp.salary)

emp.give_raise(5000)

print("Salary after raise:", emp.salary)

# output:

# Name: Rita
# Salary before raise: 30000
# Salary after raise: 35000

