# 01 Abstract class Vehicle with abstract wheels(). Children Car (4) and Bike (2). Try Vehicle() and read the error

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


class Bike(Vehicle):
    def wheels(self):
        return 2


car = Car()
bike = Bike()

print(car.wheels())
print(bike.wheels())

# output:

# 4
# 2


v = Vehicle()

# output:

# TypeError: Can't instantiate abstract class Vehicle with abstract method wheels


# 02 Put a Car and a Bike in a list and print each wheels() with a for loop

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def wheels(self):
        pass


class Car(Vehicle):
    def wheels(self):
        return 4


class Bike(Vehicle):
    def wheels(self):
        return 2


vehicles = [Car(), Bike()]

for vehicle in vehicles:
    print(vehicle.wheels())

# output:

# 4
# 2

# 03 Abstract class Employee with a normal __init__(name) and abstract salary(). Make Manager and Driver

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass


class Manager(Employee):
    def salary(self):
        return 60000


class Driver(Employee):
    def salary(self):
        return 25000


m = Manager("Ram")
d = Driver("Hari")

print(m.name, m.salary())
print(d.name, d.salary())

# output:

# Ram 60000
# Hari 25000


# 04 Class Mobile with private __battery = 100, a getter, and use(amount) that never lets the battery go below 0

class Mobile:
    def __init__(self):
        self.__battery = 100

    def get_battery(self):
        return self.__battery

    def use(self, amount):
        self.__battery -= amount

        if self.__battery < 0:
            self.__battery = 0


phone = Mobile()

print(phone.get_battery())

phone.use(30)
print(phone.get_battery())

phone.use(90)
print(phone.get_battery())

# output:

# 100
# 70
# 0

# 05 Add withdraw(amount) to the BankAccount. Refuse if the amount is more than the balance

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdraw successful")


account = BankAccount(5000)

account.withdraw(2000)
print(account.balance)

account.withdraw(4000)
print(account.balance)

# output:

# Withdraw successful
# 3000
# Insufficient balance
# 3000

# 06 Class User with private __password and login(password) that prints "Welcome" or "Wrong password"

class User:
    def __init__(self, password):
        self.__password = password

    def login(self, password):
        if password == self.__password:
            print("Welcome")
        else:
            print("Wrong password")


user = User("python123")

user.login("abc")
user.login("python123")

# output:

# Wrong password
# Welcome