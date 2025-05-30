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
        elif choice equal to "P"
            result = determine_grade(score)
        elif choice equal to "S"
            print_line(score)
        else
            display "Invalid choice"
        display menu
        get choice
    display "farewell"
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
        elif choice == "S":
            print_line(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter choice: ").upper()
    print("farewell")
main()
