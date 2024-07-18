def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]


def palindrome_checker():
    print("Palindrome Checker")
    user_input = input("Enter a string to check: ")
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.")


palindrome_checker()

# This program checks if a given string is a palindrome.
# It takes a user input string, cleans it by removing non-alphanumeric characters and converting to lowercase.
# The cleaned string is then compared with its reverse to check for palindrome.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
