# Creating Dictionaries.
# Dictionaries are created using curly braces {} and consist of key-value pairs
empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "New York"}


# Accessing Elements.
# Elements are accessed using keys.
print(person["name"])  # Output: Alice


# Modifying Elements.
# Elements can be modified by accessing them directly via their keys.
person["age"] = 30
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Adding Elements
# New key-value pairs can be added directly.
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


# Removing Elements
# pop(): Removes the element with the specified key and returns its value.
# popitem(): Removes the last inserted key-value pair.
# del: Deletes an element by key or clears the entire dictionary.
# clear(): Removes all elements.
age = person.pop("age")
print(age)  # Output: 25
person.popitem()
del person["name"]
person.clear()
print(person)  # Output: {}


# Dictionary Methods
# keys(): Returns a view object of all keys.
# values(): Returns a view object of all values.
# items(): Returns a view object of all key-value pairs.
# update(): Updates the dictionary with elements from another dictionary or iterable of key-value pairs.
# get(): Returns the value for the specified key.
person = {"name": "Alice", "age": 25}
print(person.keys())    # Output: dict_keys(['name', 'age'])
print(person.values())  # Output: dict_values(['Alice', 25])
print(person.items())   # Output: dict_items([('name', 'Alice'), ('age', 25)])
person.update({"city": "New York"})
print(person)           # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(person.get("name"))  # Output: Alice


# Looping Through Dictionaries
# Loop through keys, values, or key-value pairs.
person = {"name": "Alice", "age": 25, "city": "New York"}
for key in person:
    print(key)
for value in person.values():
    print(value)
for key, value in person.items():
    print(key, value)

# These are the basic concepts and usage examples of dictionaries in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
