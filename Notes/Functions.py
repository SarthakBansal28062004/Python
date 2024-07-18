# Defining a Function -> Functions are defined using the def keyword followed by the function name and parentheses ()

# Syntax
# def function_name(parameters):
#     block of code
#     return value

def greet():
    print("Hello, World!")

# Calling a Function
# Functions are called by their name followed by parentheses ()
greet()  # Output: Hello, World!


# Parameters and Arguments

# Positional Arguments -> Arguments that are passed to the function in the same order as the parameters
def greet(name):
    print("Hello, " + name + "!")
greet("Sarthak")  # Output: Hello, Sarthak!

# Default Arguments -> Parameters can have default values
def greet(name="Coder"):
    print("Hello, " + name + "!")
greet()           # Output: Hello, Coder!
greet("Sarthak")    # Output: Hello, Sarthak!

# Keyword Arguments -> Arguments can be passed by specifying the parameter names
def greet(first_name, last_name):
    print("Hello, " + first_name + " " + last_name + "!")
greet(first_name="Sarthak", last_name="Bansal")  # Output: Hello, Sarthak Bansal!


# Return Statement

# Returning Values -> Functions can return values using the return keyword
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8


# Variable Scope

# Local Variables -> Variables defined inside a function are local to that function
def my_function():
    x = 10  # Local variable
    print(x)
my_function()
# print(x)  # Error: x is not defined outside the function

# Global Variables -> Variables defined outside all functions are global and can be accessed inside functions
x = 10  # Global variable
def my_function():
    print(x)
my_function()  # Output: 10


# Nested Functions

# Function within a Function -> Functions can be defined inside other functions
def outer_function():
    def inner_function():
        print("Hello, Inner World!")
    inner_function()
outer_function()  # Output: Hello, Inner World!


# These are the basic concepts and usage examples of functions in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
