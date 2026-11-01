#  The menu is a dictionary (Day 06). A wrong item gives a KeyError, a wrong quantity gives a ValueError. else adds to the bill only when both worked.

# Your job:
# 1. if qty is 0 or less, raise ValueError("Quantity
#    must be more than 0"), and print e in except
# 2. save each order in a list and print it at the end


menu = {
    "veg momo": 120,
    "chicken momo": 180,
    "chowmein": 150
}

total = 0
orders = []

print("=== MOMO HOUSE ===")
for item, price in menu.items():
    print(f"- {item}: Rs. {price}")

while True:
    item = input("Item (or done): ").strip().lower()

    if item == "done":
        break

    try:
        price = menu[item]
        qty = int(input("How many? "))

        if qty <= 0:
            raise ValueError("Quantity must be more than 0")

    except KeyError:
        print("Sorry, we don't have", item)

    except ValueError as e:
        print(e)

    else:
        total += price * qty
        orders.append((item, qty, price * qty))
        print(f"Added {qty} x {item}")

print("\n=== ORDER SUMMARY ===")

if orders:
    for item, qty, subtotal in orders:
        print(f"{qty} x {item} = Rs. {subtotal}")
else:
    print("No items ordered.")

print("Total bill: Rs.", total)


# output:

# === MOMO HOUSE ===
# - veg momo: Rs. 120
# - chicken momo: Rs. 180
# - chowmein: Rs. 150

# Item (or done): pizza
# Sorry, we don't have pizza

# Item (or done): veg momo
# How many? 0
# Quantity must be more than 0

# Item (or done): veg momo
# How many? two
# invalid literal for int() with base 10: 'two'

# Item (or done): veg momo
# How many? 2
# Added 2 x veg momo

# Item (or done): done

# === ORDER SUMMARY ===
# 2 x veg momo = Rs. 240
# Total bill: Rs. 240