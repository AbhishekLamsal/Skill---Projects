# Scores live in a Day 06 dictionary. sorted() with reverse=True puts the biggest first, and slicing [:3] from Day 04 takes the top 3.
# Your job:
# 1. print every name A to Z, numbered with enumerate()
# 2. print who came last, with min(..., key=scores.get)

scores = {
    "Ram": 450,
    "Sita": 720,
    "Hari": 380,
    "Gita": 610
}

top = sorted(scores.values(), reverse=True)

print(f"Top 3 scores: {top[:3]}")
print(f"Players: {len(scores)}")
print(f"Total points: {sum(scores.values())}")

print(f"Winner: {max(scores, key=scores.get)}")

for num, name in enumerate(sorted(scores), start=1):
    print(f"{num}. {name}")

print(f"Last place: {min(scores, key=scores.get)}")