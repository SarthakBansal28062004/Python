# Importing necessary python modules
import time

# Syntax: print(object(s), sep=separator, end=end, file=file, flush=flush)
print("Hello, World!")

# You can print multiple objects by separating them with commas.
print("Hello", "World", 2024)

# By default, objects are separated by a space.
# You can change the separator using the sep parameter.
print("Hello", "World", sep="-")

# By default, the print statement ends with a newline character (\n).
# You can change the ending character using the end parameter.
print("Hello", end=" ")
print("World")

# You can direct the output of the print statement to a file.
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)
# This will write Hello, World! to output.txt.

# The flush parameter controls whether the output is buffered or not.
# By default, it is False, meaning the output is buffered.
# Setting it to True forces the print statement to flush the buffer.
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)
    print()
# This will print the numbers 0 to 4 with a 1-second interval without buffering the output.

# Use of special characters- Newline: \n and Tab: \t
print("Hello\nWorld")
print("Hello\tWorld")

# You can directly print the values of variables.
x = 30
y = 55
print("x =", x, "and y =", y)

# These are the basic concepts and usage examples of print statements in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
