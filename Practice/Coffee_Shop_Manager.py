# Defining Coffe Shop Class
class CoffeeShop:

    # Attributes such as menu, inventory, and sales
    def __init__(self):

        # Coffee Shop Menu
        self.menu = {
            "espresso": 200.0,
            "cold brew": 150.0,
            "cappuccino": 220.0,
            "mocha": 170.0,
            "lattes": 150.0,
            "breve": 200.0,
        }

        # Coffee Shop Inventory
        self.inventory = {
            "espresso": 50,
            "cold brew": 50,
            "cappuccino": 50,
            "mocha": 50,
            "lattes": 50,
            "breve": 50,
        }

        # Net Sales (Initialized with 0)
        self.sales = 0.0

    # Function to display the menu
    def display_menu(self):

        print("\n☕️---- Our Menu ----☕️\n")

        # Printing all the items along with their price
        for coffee, price in self.menu.items():
            print(f"{coffee.capitalize()}: Rs {price}")

        print("\n---- Please Select Any One Coffee Of Your Choice ----\n")

    # Function to take orders from customers
    def take_order(self):

        # Call display_menu() to show different types of coffee to the customers
        self.display_menu()

        # Taking order from the customer
        order = input("What Would You Like To Have 😇: ").lower()

        # Check for valid order from the customer

        if order in self.menu:

            if self.inventory[order] > 0:

                quantity = int(input(f"\nHow many {order} would you love to have 😇: "))

                if quantity <= self.inventory[order]:

                    self.process_order(order, quantity)

                else:

                    print(f"\nSorry! We are out of {order} as per your needs 😞")
                    print(f"We currently have {self.inventory[order]} left 😇")

            else:

                print(f"\nSorry! We don't have any inventory left for {order} 😞")

        else:

            print("\nSorry! But we do not have such item in our menu 😞")

    # Function for processing the order
    def process_order(self, order, quantity):

        # Total cost for the order
        cost = self.menu[order] * quantity

        # Printing Order Details
        print(f"\nYour Order: {quantity} {order}(s) for Rs {cost + 10.5} including all taxes 😉")

        # Getting order confirmation
        confirm = input("\nWould you like to proceed with order? (Yes/No): ").lower()

        # Check confirmation given by the customer
        if confirm == "yes":

            # Update sales and inventory
            self.sales += cost
            self.inventory[order] -= quantity

            # Order processed successfully
            print("\nThank You, your order has processed successfully 🥰")

        else:

            print("\nOrder Canceled")

    # Function to display sales
    def display_sales(self):

        print(f"Gross Sales: Rs {self.sales}")

    # Function to show leftover inventory
    def show_inventory(self):

        print("\n📦---- Inventory ----📦\n")

        # Display the inventory
        for coffee, quantity in self.inventory.items():

            print(f"{coffee.capitalize()}: {quantity}")


# Main function for user interaction
def main():

    # Creating an object for the coffee shop
    shop = CoffeeShop()

    while True:

        print("\nWelcome to Sarthak's Coffee Shop\n")

        # Give choices to the customers
        print("1. Placing an order")
        print("2. View Sales")
        print("3. View Inventory")
        print("4. Exit")

        # Take customer's choice
        choice = input("\nEnter A Choice: ")

        # Based on customer's choice
        if choice == "1":
            shop.take_order()

        elif choice == "2":
            shop.display_sales()

        elif choice == "3":
            shop.show_inventory()

        elif choice == "4":
            print("Thank You Visiting Us 😇")
            break

        else:
            print("\nPlease enter a valid choice")


# Add code running script (To run code)
if __name__ == "__main__":
    main()

# Program Ends

# This program is a Coffee Shop Management System.
# It allows the user to place orders, view sales, and check the inventory.
# The CoffeeShop class handles the core functionality, including managing the menu, processing orders,
# and updating sales and inventory.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
