# # name = "nepal"
# # fruits = ["mango", "apple"]

# # # Function: name(value)
# # print(len(name))          # 5
# # print(len(fruits))        # 2

# # # Method: value.name()
# # print(name.upper())       # NEPAL
# # fruits.append("banana")
# # print(fruits)             # ['mango', 'apple', 'banana']



# # print("a", "b", "c")
# # print(sum(dict1.value()))


# print("Ram", "Sita", "Hari")
# # Ram Sita Hari

# print("Ram", "Sita", "Hari", sep=", ")
# # Ram, Sita, Hari

# print("2026", "10", "01", sep="-")
# # 2026-10-01

# for i in range(1, 6):
#     print(i, end=" ")
# # 1 2 3 4 5

# ask = input("What is your name? ")
# print(ask)


# def average(numbers):
#     return round(sum(numbers) / len(numbers), 2)

# marks = [67, 45, 92, 78, 55]
# print(average(marks))          
fruits = ["apple", "mango", "banana"]
for num, fruit in enumerate(fruits):
    print(f"{num}. {fruit}") 