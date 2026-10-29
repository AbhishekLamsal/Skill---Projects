# The menu is a Day 06 dictionary. Sort it by price, find cheap items with filter(), raise every price with map(), and find the costliest item with max().

# Your job:
# 1. print the total of all prices with sum()
# 2. ask the user for a budget with int(input())
#    and show only the items they can buy


menu = {
    "momo": 150,
    "chowmein": 120,
    "tea": 30,
    "lassi": 80,
    "pizza": 450
}

print("--- Cheapest first ---")
for item, price in sorted(menu.items(), key=lambda x: x[1]):
    print(f"{item}: Rs. {price}")

cheap = list(filter(lambda item: menu[item] < 100, menu))
print("Under Rs. 100:", cheap)

new_prices = list(map(lambda p: p + 10, menu.values()))
print("New prices:", new_prices)

costliest = max(menu, key=lambda item: menu[item])
print("Costliest:", costliest)

total = sum(menu.values())
print("Total of all prices:", total)

budget = int(input("Enter your budget: "))

affordable = list(filter(lambda item: menu[item] <= budget, menu))

print("You can buy:")
for item in affordable:
    print(f"{item}: Rs. {menu[item]}")


# output

# --- Cheapest first ---
# tea: Rs. 30
# lassi: Rs. 80
# chowmein: Rs. 120
# momo: Rs. 150
# pizza: Rs. 450
# Under Rs. 100: ['tea', 'lassi']
# New prices: [160, 130, 40, 90, 460]
# Costliest: pizza
# Total of all prices: 830
# Enter your budget: 1000
# You can buy:
# momo: Rs. 150
# chowmein: Rs. 120
# tea: Rs. 30
# lassi: Rs. 80
# pizza: Rs. 450