#   Two lists: items and prices. show_bill() walks them together with zip(). bill_total() uses sum() and round(), with a default discount of 0, like Day 09.
# Your job:
# 1. number every line with enumerate(items, start=1)
# 2. print the cheapest item's name
#    (hint: prices.index(min(prices)) from Day 04)

def show_bill(items, prices):
    print("------ BILL ------")
    for num, (item, price) in enumerate(zip(items, prices), start=1):
        print(f"{num}. {item}: Rs. {price}")
    print("------------------")

def bill_total(prices, discount=0):
    total = sum(prices)
    return round(total - total * discount / 100, 2)

items = ["rice", "oil", "sugar", "tea"]
prices = [1200, 350, 140, 260]

show_bill(items, prices)

print(f"Items: {len(items)}")
print(f"Costliest: Rs. {max(prices)}")

cheapest_index = prices.index(min(prices))
print(f"Cheapest item: {items[cheapest_index]}")

print(f"Total: Rs. {bill_total(prices)}")
print(f"After 10% off: Rs. {bill_total(prices, 10)}")