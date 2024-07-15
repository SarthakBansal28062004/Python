# Basic Data Types

# Integer (int) -> Represents whole numbers without a decimal point.
x = 10
y = -5
print(type(x))  # <class 'int'>

# Floating Point (float) -> Represents real numbers with a decimal point.
pi = 3.14
gravity = 9.8
print(type(pi))  # <class 'float'>

# String (str) -> Represents a sequence of characters.
# Strings are immutable, meaning they cannot be changed after they are created.
name = "Alice"
greeting = 'Hello, World!'
print(type(name))  # <class 'str'>

# Boolean (bool) -> Represents two values: True or False.
is_active = True
has_permission = False
print(type(is_active))  # <class 'bool'>


# Collection Data Types

# List (list) -> An ordered collection of items which can be of different types.
# Lists are mutable, meaning they can be changed after they are created.
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(type(fruits))  # <class 'list'>

# Tuple (tuple) -> An ordered collection of items which can be of different types.
# Tuples are immutable, meaning they cannot be changed after they are created.
point = (10, 20)
colors = ("red", "green", "blue")
print(type(point))  # <class 'tuple'>

# Dictionary (dict) -> A collection of key-value pairs.
# Dictionaries are unordered and mutable.
person = {"name": "Alice", "age": 25, "city": "New York"}
print(type(person))  # <class 'dict'>

# Set (set) -> An unordered collection of unique items.
# Sets are mutable.
fruits = {"apple", "banana", "cherry"}
unique_numbers = {1, 2, 3, 4, 5}
print(type(fruits))  # <class 'set'>


# Other Data Types

# None Type (NoneType) -> Represents the absence of a value or a null value.
result = None
print(type(result))  # <class 'NoneType'>


# Type Conversion
# You can convert between different data types using built-in functions.

# Integer to String
x = 10
x_str = str(x)
print(type(x_str))  # <class 'str'>

# String to Integer
x_str = "10"
x = int(x_str)
print(type(x))  # <class 'int'>

# String to Float
pi_str = "3.14"
pi = float(pi_str)
print(type(pi))  # <class 'float'>

# List to Tuple
fruits = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits)
print(type(fruits_tuple))  # <class 'tuple'>

# Tuple to List
point = (10, 20)
point_list = list(point)
print(type(point_list))  # <class 'list'>

# List to Set
fruits = ["apple", "banana", "cherry", "apple"]
fruits_set = set(fruits)
print(type(fruits_set))  # <class 'set'>


# Checking Data Type
# You can check the type of variable using the type() function.
x = 10
print(type(x))  # <class 'int'>

# These are the basic concepts and usage examples of data types in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
