#  01 Write multiply(*nums) that multiplies all the numbers. multiply(2, 3, 4) gives 24

def multiply(*nums):
    result = 1

    for num in nums:
        result *= num

    return result


print(multiply(2, 3, 4))
'''
    output
24
   '''

# 02 Write biggest(*nums) that returns the biggest number, or None if nothing is sent

def biggest(*nums):
    if len(nums) == 0:
        return None

    return max(nums)

print(biggest(10, 5, 99, 23))
print(biggest())

'''
    output
99
None
   '''

# 03 Write make_card(**info) that prints each detail on its own line

def make_card(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


make_card(
    name="Ram",
    age=21,
    city="Pokhara"
)

'''
    output
name: Ram
age: 21
city: Pokhara
   '''

# 04 Write count_long(*words) that counts the words longer than 4 letters

def count_long(*words):
    count = 0

    for word in words:
        if len(word) > 4:
            count += 1

    return count


print(count_long("apple", "cat", "python", "sun"))

'''
    output
2
   '''

# 05 Use print(*list, sep=", ") to print your 5 favourite foods in one clean line

foods = ["momo", "pizza", "burger", "chowmein", "lassi"]

print(*foods, sep=", ")

'''
    output
momo, pizza, burger, chowmein, lassi
   '''

# 06 Add **options to your Day 09 calculator, like round_to=2

def calculator(a, b, operation, **options):
    match operation:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            if b == 0:
                return "Can't divide by 0"
            result = a / b
        case "**":
            result = a ** b
        case _:
            return "Unknown sign"

    if "round_to" in options:
        result = round(result, options["round_to"])

    return result


while True:
    op = input("Choose + - * / ** (or q to quit): ")

    if op == "q":
        print("Bye!")
        break

    x = float(input("First number: "))
    y = float(input("Second number: "))

    print(calculator(x, y, op, round_to=2))

    '''
    output
Choose + - * / ** (or q to quit): *  
First number: 45
Second number: 89
4005.0
Choose + - * / ** (or q to quit): 15
First number: 56
Second number: 55
Unknown sign
Choose + - * / ** (or q to quit): /  
First number: 78
Second number: 2
39.0
Choose + - * / ** (or q to quit): q
Bye!

   '''