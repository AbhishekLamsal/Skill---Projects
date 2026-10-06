# stats() takes any amount of numbers and returns three answers. Unpack them like Day 05. If nothing is sent, return None.
# Your job:
# 1. make a list marks = [67, 45, 92, 78]
#    and call stats(*marks)
# 2. also return how many numbers were sent

def stats(*numbers):
    if len(numbers) == 0:
        return None

    average = round(sum(numbers) / len(numbers), 2)
    return min(numbers), max(numbers), average, len(numbers)

low, high, avg, count = stats(12, 45, 7, 30)

print(f"Low: {low}, High: {high}, Average: {avg}, Count: {count}")

print(stats())

marks = [67, 45, 92, 78]
low, high, avg, count = stats(*marks)
print(f"Low: {low}, High: {high}, Average: {avg}, Count: {count}")

'''
    output
Low: 7, High: 45, Average: 23.5, Count: 4
None
Low: 45, High: 92, Average: 70.5, Count: 4
   '''