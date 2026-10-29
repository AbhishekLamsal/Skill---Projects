# The @receipt decorator prints the shop name before the order and a thank-you after it. The order() function stays small and only works out the bill. *args, **kwargs pass the inputs through, and the bill is returned.

# Your job:
# 1. write pay(amount) that prints "Paid Rs. ..."
#    and decorate it with @receipt too
# 2. write a @discount decorator that returns
#    the total minus 10% (hint: result * 0.9)


def receipt(func):
    def wrapper(*args, **kwargs):
        print("=" * 24)
        print("      MOMO HOUSE")
        print("=" * 24)

        result = func(*args, **kwargs)

        print("-" * 24)
        print("Thank you! Visit again")

        return result

    return wrapper


def discount(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 0.9  # 10% discount

    return wrapper


@receipt
@discount
def order(item, qty, price):
    total = qty * price
    print(f"{item} x {qty} = Rs. {total}")
    return total


@receipt
def pay(amount):
    print(f"Paid Rs. {amount}")
    return amount


bill = order("Chicken momo", 2, 180)

print(f"Saved bill: {bill}")

pay(bill)


# output

#      MOMO HOUSE
# ========================
# Chicken momo x 2 = Rs. 360
# ------------------------
# Thank you! Visit again
# Saved bill: 324.0
# ========================
#       MOMO HOUSE
# ========================
# Paid Rs. 324.0
# ------------------------
# Thank you! Visit again