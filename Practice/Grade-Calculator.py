def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter the score (0-100): "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The grade for score {score} is: {grade}")
    else:
        print("Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid score.")

# This is a grade calculator which tells your grade on the basis of your score
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
