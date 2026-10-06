# 01 Ask for 5 numbers, save them in a list, then print min, max, sum and the average

numbers = []

for i in range(5):
    numbers.append(int(input(f"Number {i + 1}: ")))

print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# 02 Print a numbered shopping list with enumerate(start=1)

shopping = ["Rice", "Milk", "Bread", "Eggs"]

for num, item in enumerate(shopping, start=1):
    print(f"{num}. {item}")

# 03 Use zip() to print every student's name with their city

students = ["Ram", "Sita", "Hari"]
cities = ["Kathmandu", "Pokhara", "Biratnagar"]

for name, city in zip(students, cities):
    print(f"{name} - {city}")

# 04 Use all() to check if every price in a list is under Rs. 500

prices = [250, 400, 150, 499]

if all(price < 500 for price in prices):
    print("All prices are under Rs. 500")
else:
    print("Some prices are Rs. 500 or more")

# 05 Turn 10000 seconds into hours, minutes and seconds with divmod()

seconds = 10000

minutes, secs = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f"{hours} h {minutes} m {secs} s")

# 06 Find the longest name in a list with max(names, key=len) 

names = ["Ram", "Sita", "Krish", "Alexandra", "Hari"]

print("Longest name:", max(names, key=len))