# Creating Lists
# They can be created using square brackets [] and can contain elements of any type
empty_list = []
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "Hello", 3.14, True]

# Accessing Elements
# These in a list can be accessed using indexing. Indexing starts at 0
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1])  # Output: cherry (negative indexing)

# Modifying Elements
# It can be modified by accessing them directly via their index.
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']


# List Slicing
# Subsets of the list can be accessed using slicing
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[:2])   # Output: ['apple', 'banana']
print(fruits[2:])   # Output: ['cherry', 'date']
print(fruits[::2])  # Output: ['apple', 'cherry']


# Adding Elements
# append(): Adds an element to the end of the list.
# insert(): Adds an element at a specified position.
# extend(): Adds elements from another list.
fruit = ["apple", "banana", "cherry"]
fruit.insert(1, "blueberry")
fruit.append("strawberry")
fruit.extend(["date", "elderberry"])
print(fruit)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'strawberry', 'date', 'elderberry']


# Removing Elements
# remove(): Removes the first occurrence of a value.
# pop(): Removes and returns the element at a specified position (default is the last element).
# del: Deletes an element or slice.
# clear(): Removes all elements from the list.
fruits = ["apple", "banana", "cherry", "date"]
fruits.remove("banana")
fruits.pop(2)
del fruits[0]
fruits.clear()
print(fruits)  # Output: []


# List Methods
# len(): Returns the number of elements.
# sort(): Sorts the list.
# reverse(): Reverses the list.
# index(): Returns the index of the first occurrence of a value.
# count(): Returns the number of occurrences of a value.
fruits = ["cherry", "banana", "apple", "date"]
print(len(fruits))      # Output: 4
fruits.sort()
print(fruits)           # Output: ['apple', 'banana', 'cherry', 'date']
fruits.reverse()
print(fruits)           # Output: ['date', 'cherry', 'banana', 'apple']
print(fruits.index("banana"))  # Output: 2
print(fruits.count("apple"))   # Output: 1


# List Comprehensions
# A concise way to create lists
squares = [x ** 2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# These are the basic concepts and usage examples of strings in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
