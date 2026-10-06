# make_bill() takes any number of prices with *prices, and a discount that must be sent by name. Day 07 if checks for an empty cart. Day 10 built-ins do the maths.
# Your job:
# 1. call make_bill() with no prices. What happens?
# 2. ask the user for prices with input().split(),
#    turn each one into an int (Day 10 project),
#    then send them with make_bill(*prices)

def make_bill(*prices, discount=0):
    if not prices:
        print("Cart is empty!")
        return 0
# pay = make_bill()
# print(pay)
    ''' output
    Cart is empty!
    0
    '''

    total = sum(prices)
    saved = total * discount / 100

    print(f"Items:     {len(prices)}")
    print(f"Costliest: Rs. {max(prices)}")
    print(f"Total:     Rs. {total}")
    print(f"Discount:  Rs. {round(saved, 2)}")
    return round(total - saved, 2)
user_input = input("Enter prices separated by spaces: ")
prices = [int(price) for price in user_input.split()]
pay = make_bill(*prices)
print(f"To pay:    Rs. {pay}")

''' 
    output
Enter prices separated by spaces: 789 456 123 357 159
Items:     5
Costliest: Rs. 789
Total:     Rs. 1884
Discount:  Rs. 0.0
To pay:    Rs. 1884.0
    '''