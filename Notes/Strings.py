# Creating Strings
# It can be created using single quotes, double quotes, or triple quotes for multi-line strings
single_quote_str = 'Hello'
double_quote_str = "Hello"
triple_quote_str = """Hello
World"""

# Accessing Characters - in a string can be done using indexing.
# Indexing starts at 0
s = "Hello"
print(s[0])  # Output: H
print(s[1])  # Output: e

# Slicing Strings
# Substrings can be extracted using slicing.
# Syntax - substring = string[start:stop:step]
s = "Hello, World!"
print(s[0:5])     # Output: Hello
print(s[:5])      # Output: Hello
print(s[7:])      # Output: World!
print(s[::2])     # Output: Hlo ol!


# String Methods

# len() - Returns the length of the string
s = "Hello"
print(len(s))  # Output: 5

# str.upper(), str.lower() - Converts all characters in the string to upper or lower case
s = "Hello"
print(s.upper())  # Output: HELLO
print(s.lower())  # Output: hello

# str.strip() - Removes leading and trailing whitespace
s = "  Hello  "
print(s.strip())  # Output: Hello

# str.replace() - Replaces a substring with another substring
s = "Hello, World!"
print(s.replace("World", "Python"))  # Output: Hello, Python!

# str.split() - Splits the string into a list of substrings based on a delimiter
s = "Hello, World!"
print(s.split(", "))  # Output: ['Hello', 'World!']

# str.join() - Joins a list of strings into a single string with a specified separator
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World


# Escape Characters - Special characters in strings
newline = "Hello\nWorld"
tab = "Hello\tWorld"
backslash = "This is a backslash: \\"
print(newline)
print(tab)
print(backslash)


# Multi-line Strings - Strings can span multiple lines using triple quotes
multi_line_str = """This is a string
that spans multiple
lines."""
print(multi_line_str)

# Raw Strings - Prefixing a string with r or R to treat backslashes as literal characters
raw_str = r"C:\Users\Name"
print(raw_str)  # Output: C:\Users\Name

# These are the basic concepts and usage examples of strings in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
