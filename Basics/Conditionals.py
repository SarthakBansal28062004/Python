# Basic Conditional Statements

# If Statement -> Executes a block of code if a specified condition is True
x = 10
if x > 5:
    print("x is greater than 5")

# If-else Statement -> Executes one block of code if the condition is True and another block if it is False
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# If-elif-else Statement -> Executes different blocks of code for different conditions
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# Nested Conditional Statements

# Nested If Statements -> You can place an if statement inside another if statement
x = 10
if x > 5:
    print("x is greater than 5")
    if x == 10:
        print("x is equal to 10")

# Combined Conditions (and, or, not)
x = 10
y = 5
if x > 5 and y > 2:
    print("Both conditions are true")

# Ternary Conditional Operator -> Provides a concise way to write conditional statements with a single line
# result = value_if_true if condition else value_if_false
x = 10
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(result)

# Special Case: pass Statement
# pass is a null operation. It does nothing when executed.
# Useful as a placeholder where syntactically a statement is required, but you have nothing to execute.
x = 10
if x > 5:
    pass  # Do nothing
else:
    print("x is not greater than 5")

# Checking Truth Value
# In Python, values that evaluate to False in conditional statements:
# False, None, 0 (integer), 0.0 (float), "" (empty string), [] (empty list),
# {} (empty dictionary), set() (empty set)

# Comparison Operators
# Comparison operators (>, <, >=, <=, ==, !=) are used to compare values.
x = 10
y = 5
if x > y:
    print("x is greater than y")

# These are the basic concepts and usage examples of conditionals in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
