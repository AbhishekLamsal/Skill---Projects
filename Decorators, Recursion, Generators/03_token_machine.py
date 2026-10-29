# The generator never ends (while True), but it only makes a new token when next() asks. A while loop (Day 08) keeps asking until the user types q.

# Your job:
# 1. make a second machine for VIP customers: "V"
#    ask "normal or vip?" and use the right one
# 2. write a generator countdown(n) that yields
#    n down to 1, and print: Next in 3 2 1


def token_machine(prefix):
    n = 1

    while True:
        yield f"{prefix}-{n}"
        n += 1


def countdown(n):
    while n >= 1:
        yield n
        n -= 1


normal_tokens = token_machine("A")
vip_tokens = token_machine("V")

print(f"=== Bank Token Machine ===")

while True:
    choice = input("Normal or VIP? (n/v, q to quit): ").lower()

    if choice == "q":
        print(f"Bye!")
        break

    if choice == "n":
        print(f"Your token: {next(normal_tokens)}")
    elif choice == "v":
        print(f"Your token: {next(vip_tokens)}")
    else:
        print(f"Please choose n, v, or q")
        continue

    print(f"Next in ", end="")
    for number in countdown(3):
        print(f"{number}", end=" ")
    print()

# output

# === Bank Token Machine ===
# Normal or VIP? (n/v, q to quit): n
# Your token: A-1
# Next in 3 2 1 
# Normal or VIP? (n/v, q to quit): v
# Your token: V-1
# Next in 3 2 1 
# Normal or VIP? (n/v, q to quit): q
# Bye!