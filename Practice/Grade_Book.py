def display_grades(grade_book):
    print("Grade Book:")
    for student, grades in grade_book.items():
        print(f"{student}: {grades}")


def average_grade(grades):
    return sum(grades) / len(grades) if grades else 0


def grade_book():
    grade_book = {}
    print("Grade Book Manager")

    while True:
        action = input("Choose an action: add, display, average, quit: ").strip().lower()

        if action == 'add':
            student = input("Enter student name: ")
            grades = input("Enter grades separated by spaces: ").split()
            grades = list(map(int, grades))
            grade_book[student] = grades
        elif action == 'display':
            display_grades(grade_book)
        elif action == 'average':
            student = input("Enter student name to calculate average grade: ")
            if student in grade_book:
                avg = average_grade(grade_book[student])
                print(f"Average grade for {student}: {avg:.2f}")
            else:
                print(f"{student} is not in the grade book.")
        elif action == 'quit':
            print("Exiting the Grade Book Manager.")
            break
        else:
            print("Invalid action selected.")


grade_book()

# This program manages a grade book.
# It allows the user to add student grades, display all grades, and calculate the average grade for a student.
# The grades are stored in a dictionary with student names as keys and lists of grades as values.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn: https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python.

# Thank You for reading my notes. It means a lot!
