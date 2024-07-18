def display_list(shopping_list):
    print("Your Shopping List:")
    for item in shopping_list:
        print(f"- {item}")


def shopping_list_manager():
    shopping_list = []
    print("Shopping List Manager")

    while True:
        action = input("Choose an action: add, remove, display, quit: ").strip().lower()

        if action == 'add':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif action == 'remove':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} is not in the shopping list")
        elif action == 'display':
            display_list(shopping_list)
        elif action == 'quit':
            print("Exiting the Shopping List Manager")
            break
        else:
            print("Invalid action selected")


shopping_list_manager()

# This program manages a shopping list.
# It allows the user to add, remove, and display items in the shopping list.
# The list is maintained using basic list operations in Python.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.
