text = input("Enter marks with spaces: ")

marks = list(map(int, text.split()))

print(f"Students: {len(marks)}")
print(f"Highest:  {max(marks)}")
print(f"Lowest:   {min(marks)}")
print(f"Total:    {sum(marks)}")
print(f"Average:  {round(sum(marks) / len(marks), 2)}")
print(f"Sorted:   {sorted(marks, reverse=True)}")

print(f"Passed:   {sum(mark >= 40 for mark in marks)}")

if all(mark >= 40 for mark in marks):
    print("Everyone passed!")