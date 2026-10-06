# Build your own mini print(): any number of words with *words, then sep and end that must be sent by name, just like the real print() from Day 10.
# Your job:
# 1. add times=1, and print the line that many times
# 2. what happens with shout(5, 10)? Fix it with str()

def shout(*words, sep=" ", end="!", times=1):
    words = [str(word) for word in words] # fix for shout(5, 10)
    text = sep.join(words).upper() + end
    print(text)

shout("hello", "class")
shout("python", "is", "fun", sep="-")
shout("namaste", end="!!!")

words = ["we", "love", "momo"]
shout(*words)

# Task 1: Print multiple times
shout("study", "hard", times=3)

# Task 2
shout(5, 10)

'''
    output: when word is not fixed with str().
TypeError: sequence item 0: expected str instance, int found
   '''

'''
    output: when word is fixed with str().
HELLO CLASS!
PYTHON-IS-FUN!
NAMASTE!!!
WE LOVE MOMO!
STUDY HARD!
5 10!
   '''  