MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main():
    """Get score, determine grade and get random_score, random_grade"""
    score = get_valid_score()
    grade = determine_grade(score)
    print(f"{score} - {grade}")

def determine_grade(score):
    """Determine grade based on score"""
    if score >= EXCELLENT_THRESHOLD:
        grade = "Excellent"
    elif score >= PASS_THRESHOLD:
        grade = "Passable"
    else:
        grade = "Bad"
    return grade

def get_valid_score():
    """Get valid score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score
main()