def display_contacts(contacts):
    print("Your Contacts:")
    for name, details in contacts:
        print(f"Name: {name}, Phone: {details[0]}, Email: {details[1]}")


def contact_book():
    contacts = []
    print("Contact Book")

    while True:
        action = input("Choose an action: add, display, quit: ").strip().lower()

        if action == 'add':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            contacts.append((name, (phone, email)))
        elif action == 'display':
            display_contacts(contacts)
        elif action == 'quit':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid action selected.")


contact_book()

# This program manages a contact book.
# It allows the user to add and display contacts, storing each contact as a tuple.
# The tuples contain the name, phone number, and email of each contact.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
