# Defining the class for home management system
class HomeManagementSystem:

    # Initializing the attributes - status for lights, alarm, appliances and temperature
    def __init__(self):

        # Describing the required attributes
        self.lights_status = False
        self.temperature = 22  # Initially set to 22^C
        self.alarm_status = False
        self.appliances_status = False

    # Using a menu to take user input to handle different cases
    @staticmethod
    def display_menu():

        # Display menu
        print("\n🏠---- Home Management System ----🏠\n")
        print("1. To Control Lights 💡")
        print("2. To Control Temperature 🌡️")
        print("3. To Control Alarm 🚨")
        print("4. To Control Appliances 🔌")
        print("5. To View Status ✨")
        print("6. To Exit ❌")
        choice = input("\nEnter your choice (1-6): ")
        return choice

    # Function to display lights menu
    @property
    def lights_menu(self):

        print("\nControl Lights")
        print("1. To Turn On 🟢")
        print("2. To Turn Off 🔴")
        print("3. To Return To Main Menu 🟠")
        choice = input("\nEnter your choice (1-3): ")
        return choice

    # Function to display temperature menu
    @property
    def temperature_menu(self):
        print("\nControl Temperature")
        print("1. To Increase 🟢")
        print("2. To Decrease 🔴")
        print("3. To Return To Main Menu 🟠")
        choice = input("\nEnter your choice (1-3): ")
        return choice

    # Function to display security menu
    @property
    def security_menu(self):
        print("\nControl Security System")
        print("1. To Arm 🟢")
        print("2. To Disarm 🔴")
        print("3. To Return To Main Menu 🟠")
        choice = input("\nEnter your choice (1-3): ")
        return choice

    # Function to display appliances menu
    @property
    def appliances_menu(self):
        print("\nControl Appliances")
        print("1. To Turn On 🟢")
        print("2. To Turn Off 🔴")
        print("3. To Return To Main Menu 🟠")
        choice = input("\nEnter your choice (1-3): ")
        return choice

    # Function to view status
    def view_status(self):

        print("\nCurrent Status")
        print(f"Lights: {'On' if self.lights_status else 'Off'}")
        print(f"Temperature: {self.temperature} Celsius")
        print(f"Security System: {'Armed' if self.alarm_status else 'Disarmed'}")
        print(f"Appliances: {'On' if self.appliances_status else 'Off'}")

    # Function to control lights
    def control_lights(self):

        while True:

            choice = self.lights_menu

            if choice == "1":
                print("Lights Turned On")
                self.lights_status = True

            elif choice == "2":
                print("Lights Turned Off")
                self.lights_status = False

            elif choice == "3":
                break

            else:
                print("Please enter a valid choice")

    # Function to control temperature
    def control_temperature(self):

        while True:

            choice = self.temperature_menu

            if choice == "1":
                self.temperature += 1
                print(f"Temperature Increased To {self.temperature} Celsius")

            elif choice == "2":
                self.temperature -= 1
                print(f"Temperature Decreased To {self.temperature} Celsius")

            elif choice == "3":
                break

            else:
                print("Please enter a valid choice")

    # Function to control security system
    def control_security(self):

        while True:

            choice = self.security_menu

            if choice == "1":
                print("Armed")
                self.alarm_status = True

            elif choice == "2":
                print("Disarmed")
                self.alarm_status = False

            elif choice == "3":
                break

            else:
                print("Please enter a valid choice")

    # Function to control appliances
    def control_appliances(self):

        while True:

            choice = self.appliances_menu

            if choice == "1":
                print("Appliances Turned On")
                self.appliances_status = True

            elif choice == "2":
                print("Appliances Turned Off")
                self.appliances_status = False

            elif choice == "3":
                break

            else:
                print("Please enter a valid choice")

    # Function to run system
    def run(self):

        while True:

            choice = self.display_menu()

            if choice == "1":
                self.control_lights()

            elif choice == "2":
                self.control_temperature()

            elif choice == "3":
                self.control_security()

            elif choice == "4":
                self.control_appliances()

            elif choice == "5":
                self.view_status()

            elif choice == "6":
                print("Exiting Home Management System")
                break

            else:
                print("Enter a valid choice")


# Run Code
if __name__ == "__main__":

    system = HomeManagementSystem()
    system.run()

# This program is a Home Management System.
# It allows the user to control various aspects of their home, such as lights, temperature,
# security system, and appliances.
# The HomeManagementSystem class handles the core functionality, including managing the states of
# these components and providing a user interface to interact with them.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
