# Write small functions (Day 09) that use built-ins inside: len(), set(), sorted() and max() with key=len. Then print a short report about any sentence.
# Your job:
# 1. write shortest_word(text) with min()
# 2. count how many times each word appears
#    with a dictionary (Day 06 + Day 08)

def word_count(text):
    return len(text.split())

def longest_word(text):
    return max(text.split(), key=len)

def shortest_word(text):
    return min(text.split(), key=len)

def unique_words(text):
    return sorted(set(text.lower().split()))

sentence = input("Type a sentence: ")

print(f"Letters: {len(sentence)}")
print(f"Words: {word_count(sentence)}")
print(f"Longest word: {longest_word(sentence)}")
print(f"Shortest word: {shortest_word(sentence)}")

for num, word in enumerate(unique_words(sentence), start=1):
    print(f"{num}. {word}")

counts = {}

for word in sentence.lower().split():
    counts[word] = counts.get(word, 0) + 1

print("\nWord counts:")
for word, count in sorted(counts.items()):
    print(f"{word}: {count}")
