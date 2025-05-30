"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

function main()
    display menu
    get choice
    while choice not equal to "Q"
        if choice equal to "G"
            score = get_valid_score()
        else if choice equal to "P"
            result = determine_grade(score)
        else if choice equal to "S"
            print_line(score)
        else
            display "Invalid choice"
        display menu
        get choice
    display "farewell"

function get_valid_score()
    get score
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE
        display "Invalid score"
        get score
    return score

function determine_grade(score)
    if score >= EXCELLENT_THRESHOLD
        grade = "Excellent"
    else if score >= PASS_THRESHOLD
        grade = "Passable"
    else
        grade = "Bad"
    return grade
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Displays a menu and performs tasks based on the user's selection"""
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_grade(score)
            print(f"Result of {score} is {result}")
        elif choice == "S":
            print_line(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("farewell")

def get_valid_score():
    """Get valid score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def determine_grade(score):
    """Determine result based on score"""
    if score >= EXCELLENT_THRESHOLD:
        grade = "Excellent"
    elif score >= PASS_THRESHOLD:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

main()
