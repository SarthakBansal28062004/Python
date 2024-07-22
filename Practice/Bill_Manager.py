# Import the necessary python modules
import sys


# Define the bill class
class BillingSystem:

    # Defining the attributes
    def __init__(self):

        # items to store products and amount to keep total amount
        self.items = {}
        self.total_amount = 0.0

    # function to add items
    def add_items(self, item_name, item_price, item_quantity):

        if item_name in self.items:
            self.items[item_name]['quantity'] += item_quantity
            self.items[item_name]['price'] = item_price

        else:
            self.items[item_name] = {'price': item_price, 'quantity': item_quantity}

        self.total_amount += item_price * item_quantity
        print(f"Added {item_quantity} of {item_name} at Rs {item_price} each\n")

    # function to view bill (not finalized)
    def view_bill(self):

        print("\n🧾----Current Bill----🧾\n")

        if not self.items:
            print("No items added yet\n")

        else:
            for item_name, item_info in self.items.items():
                print(f"{item_name}: {item_info['quantity']} x {item_info['price']} = "
                      f"Rs {item_info['quantity'] * item_info['price']}")

            print(f"\nTotal Amount: Rs {self.total_amount}\n")

    # function to view bill (finalized)
    def calculate_bill(self):

        print(f"\nFinal Total Amount: Rs {self.total_amount}\n")
        print("Thanks For Using The Billing Management System 😇\n")
        self.items = {}
        self.total_amount = 0.0


# Main function to run the code
def main():

    # creating the required object
    billing_system = BillingSystem()
    print("Welcome To Billing Management System\n")

    # Display menu and take user input
    while True:

        print("🔖----Menu----🔖")
        print("1. Add Item ➕")
        print("2. View Bill 🧾")
        print("3. Calculate Total 💵")
        print("4. Exit ❌\n")

        choice = input("Enter a choice: ")

        if choice == "1":
            item_name = input("Enter Name of Item: ").lower()

            try:
                item_price = float(input("Enter Price: "))
                item_quantity = int(input("Enter Quantity: "))
                billing_system.add_items(item_name, item_price, item_quantity)

            except ValueError:
                print("Invalid Input")

        elif choice == "2":
            billing_system.view_bill()

        elif choice == "3":
            billing_system.calculate_bill()

        elif choice == "4":
            print("Good Bye")
            sys.exit()

        else:
            print("Please Enter a Valid Number!")


# Run code
if __name__ == "__main__":
    main()

# This program is a Billing Management System.
# It allows the user to add items with their prices and quantities, view the current bill,
# and calculate the final bill.
# The BillingSystem class handles the core functionality, including managing items and calculating the total amount.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
