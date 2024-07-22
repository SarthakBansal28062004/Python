# Defining the class
class FitnessManagementSystem:

    # Defining the attributes
    def __init__(self):

        # To store daily logs
        self.daily_logs = []
        # goals for each day
        self.goals = {
            'calories': 0,
            'exercise_minutes': 0,
            'water_intake': 0.0,
            'meditation_minutes': 0,
            'step_count': 0
        }

    # function to set new goals
    def set_goals(self):

        print("\n💪🏻----Set Your Fitness Goals----💪🏻\n")
        self.goals['calories'] = int(input("🔥Enter The Number Of Calories To Be Burned: "))
        self.goals['exercise_minutes'] = int(input("💪🏻Enter The Number Of Minutes To Exercise: "))
        self.goals['water_intake'] = float(input("💧Enter The Liters Of Water To Drink: "))
        self.goals['meditation_minutes'] = int(input("😮‍💨Enter The Number Of Minutes To Meditate: "))
        self.goals['step_count'] = int(input("🏃🏻Enter The Number Of Steps To Walk: "))
        print("\n⚔️----Goals Set Successfully----⚔️\n")

    # function to add a daily log
    def log_entry(self):

        print("\n💨----Add Your Log----💨\n")
        date = input("📅Enter Date (YYYY-MM-DD): ")
        calories = int(input("🔥Enter Number Of Calories Burned: "))
        exercise_minutes = int(input("💪🏻Enter Minutes You Exercised: "))
        water_intake = float(input("💧Enter The Liters Of Water Drank: "))
        meditation_minutes = int(input("😮‍💨Enter Minutes You Meditated: "))
        step_count = int(input("🏃🏻Enter Steps You Walked: "))

        # Storing the log
        entry = {
            'date': date,
            'calories': calories,
            'exercise_minutes': exercise_minutes,
            'water_intake': water_intake,
            'meditation_minutes': meditation_minutes,
            'step_count': step_count
        }

        # Adding the new log to the list
        self.daily_logs.append(entry)

    # function to display fitness summary
    def display_summary(self):

        # If no logs in the list
        if not self.daily_logs:
            print("\nNo Recorded Logs\n")
            return

        # if logs in list
        print("\n🌟----Health And Fitness Summary----🌟\n")
        for log in self.daily_logs:
            print(f"Date: {log['date']}\n")
            print(f"🔥Calories Consumed: {log['calories']} / {self.goals['calories']} (Goal)")
            print(f"💪🏻Exercise Minutes: {log['exercise_minutes']} / {self.goals['exercise_minutes']} (Goal)")
            print(f"💧Water Intake: {log['water_intake']} / {self.goals['water_intake']} (Goal)")
            print(f"😮‍💨Meditation Minutes: {log['meditation_minutes']} / {self.goals['meditation_minutes']} (Goal)")
            print(f"🏃🏻Step Count: {log['step_count']} / {self.goals['step_count']} (Goal)")
            print("-" * 45)

    # function to run the code
    def start(self):

        while True:

            print("\n🌟-----Welcome To Fitness Management System-----🌟\n")
            print("1. Set Goals 🎯")
            print("2. Log Details 🔖")
            print("3. Fitness Summary 🧾")
            print("4. Exit ❌\n")

            choice = input("Enter a choice (1-4): ")

            if choice == "1":
                self.set_goals()

            elif choice == "2":
                self.log_entry()

            elif choice == "3":
                self.display_summary()

            elif choice == "4":
                print("Thanks For Using FMS ✨")
                break

            else:
                print("Please Enter a Valid Choice")


if __name__ == "__main__":
    system = FitnessManagementSystem()
    system.start()

# This program is a Fitness Management System.
# It allows the user to set fitness goals, log daily fitness activities, and view a summary of their progress.
# The FitnessManagementSystem class handles the core functionality, including managing goals,
# logging activities, and displaying summaries.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
