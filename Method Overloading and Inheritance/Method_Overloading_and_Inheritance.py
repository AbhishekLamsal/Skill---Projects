# 01 Class Calculator with multiply(self, a, b, c=1). Test it with 2 and with 3 numbers

class Calculator:
    def multiply(self, a, b, c=1):
        return a * b * c

calc = Calculator()

print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))

# Output:

# 6
# 24


# 02 Class Shop with total(self, *prices) that returns the sum of any number of prices

class Shop:
    def total(self, *prices):
        return sum(prices)

shop = Shop()

print(shop.total(10, 20, 30))
print(shop.total(5, 15, 25, 35))

# Output:

# 60
# 80


# 03 Class Shape with area() that returns 0. Children Square and Circle override area()

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


square = Square(4)
circle = Circle(3)

print("Square Area:", square.area())
print("Circle Area:", circle.area())


# Output:

# Square Area: 16
# Circle Area: 28.26


# 04 Class Person(name, age) and child Employee(name, age, salary) using super().__init__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

emp = Employee("John", 30, 50000)

print(emp.name)
print(emp.age)
print(emp.salary)

# Output:

# John
# 30
# 50000


# 05 Multilevel: Vehicle → Car → ElectricCar, each adds one method. Call all three

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")


ecar = ElectricCar()

ecar.start()
ecar.drive()
ecar.charge()

# Output:

# Vehicle started
# Car is driving
# Electric car is charging


# 06 Put a Square and a Circle in a list and print each area with a for loop

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shapes = [Square(5), Circle(3)]

for shape in shapes:
    print("Area:", shape.area())


# Output:

# Area: 25
# Area: 28.26