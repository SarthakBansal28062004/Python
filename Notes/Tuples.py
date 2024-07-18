# Creating Tuples.
# Tuples are created using parentheses () and are immutable.
empty_tuple = ()
fruits = ("apple", "banana", "cherry")
single_element_tuple = ("apple",)  # Note the comma


# Accessing Elements.
# Elements in a tuple can be accessed using indexing.
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana


# Tuple Methods
# count(): Returns the number of times a value appears.
# index(): Returns the index of the first occurrence of a value.
fruits = ("apple", "banana", "cherry", "banana")
print(fruits.count("banana"))  # Output: 2
print(fruits.index("cherry"))  # Output: 2


# Immutable Nature
# Tuples cannot be modified after creation. You cannot add, remove, or change elements.
fruits = ("apple", "banana", "cherry")
# fruits[1] = "blueberry"  # Error: 'tuple' object does not support item assignment


# Tuple Packing and Unpacking
# Packing: Creating a tuple from values.
# Unpacking: Assigning tuple elements to variables.
packed_tuple = ("apple", "banana", "cherry")
(a, b, c) = packed_tuple  # Unpacking
print(a)  # Output: apple
print(b)  # Output: banana
print(c)  # Output: cherry


# Iteration in Tuples

# Basic Iteration
# We can iterate over the elements of a tuple using a for loop
for fruit in fruits:
    print(fruit)

# Iterating with Index
# We can use the enumerate() function to get both the index and the value of each element in the tuple
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Nested Tuples
# If you have a tuple containing other tuples, you can use nested loops to iterate through the inner tuples
nested_tuples = (("apple", "banana"), ("cherry", "date"), ("elderberry", "fig"))
for inner_tuple in nested_tuples:
    for fruit in inner_tuple:
        print(fruit)

# Using while Loop
# You can also use a while loop to iterate through a tuple by maintaining an index counter
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# Iterating with zip()
# You can iterate over multiple tuples simultaneously using the zip() function
colors = ("red", "yellow", "red")
for fruit, color in zip(fruits, colors):
    print(f"The {fruit} is {color}.")

# Tuple Unpacking During Iteration
# If a tuple contains pairs or multiple elements, you can unpack the elements directly in the loop
points = ((1, 2), (3, 4), (5, 6))
for x, y in points:
    print(f"Point: ({x}, {y})")

# These are the basic concepts and usage examples of tuples in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
