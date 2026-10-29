# split() a sentence into words, then sort, filter and change them with lambdas. join() puts them back into one line.

# Your job:
# 1. count the words that start with a vowel
#    (hint: filter + w[0] in "aeiou" + len)
# 2. get the sentence from the user with input()


sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Sorted by length: {sorted(words, key=len)}")
print(f"Longest word: {max(words, key=len)}")
print(f"More than 3 letters: {list(filter(lambda w: len(w) > 3, words))}")
print(f"Capitalized: {list(map(lambda w: w.capitalize(), words))}")
print(f"Reversed words: {' '.join(map(lambda w: w[::-1], words))}")

vowel_words = list(filter(lambda w: w[0].lower() in "aeiou", words))
print(f"Words starting with a vowel: {len(vowel_words)}")

# output

# Enter a sentence: If you're testing input, then "random sentence" is simply a string containing two words.
# Sorted by length: ['a', 'If', 'is', 'two', 'then', "you're", 'input,', 'simply', 'string', 'words.', 'testing', '"random', 'sentence"', 'containing']
# Longest word: containing
# More than 3 letters: ["you're", 'testing', 'input,', 'then', '"random', 'sentence"', 'simply', 'string', 'containing', 'words.']
# Capitalized: ['If', "You're", 'Testing', 'Input,', 'Then', '"random', 'Sentence"', 'Is', 'Simply', 'A', 'String', 'Containing', 'Two', 'Words.']
# Reversed words: fI er'uoy gnitset ,tupni neht modnar" "ecnetnes si ylpmis a gnirts gniniatnoc owt .sdrow
# Words starting with a vowel: 4