# Syntax: input(prompt)
# The input() function reads a line from the input (usually from the user) and returns it as a string.
name = input("Enter your name: ")
print("Hello, " + name + "!")

# The input() function always returns a string.
# To read numbers, you need to convert the input to the appropriate type (e.g., int, float).
age = int(input("Enter your age: "))
print("You are", age, "years old.")
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# You can read multiple values from a single input line by splitting the input string.
x, y = input("Enter two numbers separated by a space: ").split()
x = int(x)
y = int(y)
print("x =", x, "y =", y)

# By default, split() uses whitespace as the separator. You can specify a different separator.
date = input("Enter a date (dd/mm/yyyy): ")
day, month, year = date.split("/")
print("Day:", day, "Month:", month, "Year:", year)

# It's important to handle cases where the user might enter invalid data.
try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")
except ValueError:
    print("Invalid input! Please enter a number.")

# You can provide default values for inputs using a workaround with the ternary operator.
name = input("Enter your name (press enter for default): ") or "Default Name"
print("Hello, " + name + "!")
# If the user presses enter without typing anything, this will output: Hello, Default Name!

# These are the basic concepts and usage examples of input statements in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
