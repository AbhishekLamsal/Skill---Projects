#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5):
    print("Hello World")


# In[3]:


for i in range(10):
    print(i)


# In[4]:


word = "Nepal"

for letter in word:
    print(letter)


# In[5]:


print(list(range(5)))


# In[6]:


print(list(range(5,1,-1)))


# In[7]:


total = 0

for num in range(1, 6):
    total += num          # same as total = total + num
    print(f"Added {num}, total is {total}")

print(f"Final total: {total}")


# In[8]:


colors = ("red", "green", "blue")     # tuple
for c in colors:
    print(c)

prices = {"tea": 20, "coffee": 50, "momo": 150}

for item in prices:                   # keys only
    print(item)

for item, price in prices.items():    # key and value
    print(f"{item}: Rs. {price}")


# In[9]:


marks = [45, 80, 32, 67, 25]
passed = 0

for m in marks:
    if m >= 40:
        print(f"{m}: Pass")
        passed += 1
    else:
        print(f"{m}: Fail")

print(f"{passed} students passed")


# In[10]:


marks = [45, 80, 32, 67, 25]
passed = 0
failed = 0

for m in marks:
    if m >= 40:
        print(f"{m}: Pass")
        passed += 1
    else:
        print(f"{m}: Fail")
        failed += 1

print(f"{passed} students passed")
print(f"{failed} students failed")


# In[13]:


count = 0
while count <= 5:
    print(count)
    count += 1


# In[15]:


tasks = []

task = input("Add a task (or 'quit'): ")

while task != "quit":
    tasks.append(task)
    task = input("Add a task (or 'quit'): ")

print("Your tasks:", tasks)


# In[16]:


numbers = [4, 9, 12, 7, 15]

for n in numbers:
    if n > 10:
        print(f"Found a big one: {n}")
        break
    print(f"{n} is small")

print("Loop over")


# In[17]:


for n in range(1, 8):
    if n == 4:
        continue        # skip 4
    print(n)


# In[19]:


while True:
    choice = input("Type 'hi' or 'exit': ").strip().lower()

    if choice == "exit":
        print("Bye!")
        break
    elif choice == "hi":
        print("Hello there!")
    else:
        print("I don't know that one")


# In[20]:


# task 2


# In[34]:


import random

secret = random.randint(1, 10)
tries = 0

while tries < 3:
    guess = int(input("Guess (1 to 10): "))
    tries += 1

    if guess == secret:
        print(f"Correct! You took {tries} tries")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
print("You exceeded your tries!")
print(f"secret number is : {secret}")
# Your job:
# 1. give only 3 tries (hint: while tries < 3)
# 2. bonus: import random
#    secret = random.randint(1, 10)

