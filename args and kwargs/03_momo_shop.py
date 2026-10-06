# place_order() uses all three: a normal box for the customer, *items for the food, and **options for extras. The menu is a Day 06 dictionary. enumerate() (Day 10) numbers each line.
# Your job:
# 1. save the returned total, then add 13% VAT
# 2. ask the user for items with input().split(),
#    then send them with place_order("You", *items)

menu = {"momo": 150, "chowmein": 120, "tea": 30, "lassi": 80}

def place_order(customer, *items, **options):
    print(f"Order for {customer}")

    total = 0

    for num, item in enumerate(items, start=1):
        if item in menu:
            print(f"{num}. {item}: Rs. {menu[item]}")
            total += menu[item]
        else:
            print(f"{num}. {item}: not on the menu")

    if options.get("delivery"):
        print("Delivery: Rs. 50")
        total += 50

    for key, value in options.items():
        if key != "delivery":
            print(f"Note: {key} = {value}")

    print(f"Total: Rs. {total}")
    return total


# Task 1
total = place_order(
    "Hari",
    "momo",
    "tea",
    "pizza",
    delivery=True,
    spicy="extra"
)

vat = total * 0.13
grand_total = total + vat

print(f"VAT (13%): Rs. {vat:.2f}")
print(f"Grand Total: Rs. {grand_total:.2f}")

print()

# Task 2
items = input("Enter items separated by spaces: ").split()

place_order("You", *items)

''' 
    output
Order for Hari
1. momo: Rs. 150
2. tea: Rs. 30
3. pizza: not on the menu
Delivery: Rs. 50
Note: spicy = extra
Total: Rs. 230
VAT (13%): Rs. 29.90
Grand Total: Rs. 259.90

Enter items separated by spaces: momo pizza burger tea lassi coke
Order for You
1. momo: Rs. 150
2. pizza: not on the menu
3. burger: not on the menu
4. tea: Rs. 30
5. lassi: Rs. 80
6. coke: not on the menu
Total: Rs. 260
   '''