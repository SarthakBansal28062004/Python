# for Loop

# Basic for Loop -> Executes a block of code a specified number of times
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() Function -> Generates a sequence of numbers.
for i in range(5):
    print(i)

# for Loop with else
# Optional else block executes when the loop completes normally (without break)
for i in range(5):
    print(i)
else:
    print("Loop finished.")


# while Loop

# Basic while Loop -> Executes a block of code as long as a specified condition is True
i = 0
while i < 5:
    print(i)
    i += 1

# while Loop with else -> Optional else block executes when the condition becomes False
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished.")


# Loop Control Statements

# break Statement -> Terminates the loop prematurely.
for i in range(5):
    if i == 3:
        break
    print(i)

# continue Statement -> Skips the remaining code inside the loop for the current
# iteration and proceeds to the next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

# pass Statement -> Placeholder that does nothing when executed.
for i in range(5):
    pass  # Do nothing


# Nested Loops

# Nested for Loops -> for loop inside another for loop.
for i in range(3):
    for j in range(2):
        print(i, j)

# Nested while Loops -> while loop inside another while loop.
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(i, j)
        j += 1
    i += 1


# Looping Through Data Structures

# Looping Through Lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping Through Strings
for char in "Python":
    print(char)

# Looping Through Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

# Looping Through Range
for i in range(1, 6):
    print(i)


# Infinite Loops

# Infinite while Loop
# while True:
#     print("Infinite loop")

# Looping with enumerate() -> Provides an index to each item of the iterable
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# These are the basic concepts and usage examples of Loops in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
