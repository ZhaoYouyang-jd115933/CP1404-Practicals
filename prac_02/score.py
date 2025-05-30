"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

function main()
    score = validate_score()
    result = determine_result(score)
    display score, result

    random_score = random.randint(0,100)
    random_result = determine_result(random_score)
    display random_score, random_result

function validate_score()
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE
        display "Invalid score"
        score = float(input("Enter score: "))
    return score

function determine_result(score)
    if score >= EXCELLENT_THRESHOLD
        result = "Excellent"
    else if score >= PASS_THRESHOLD
        result = "Passable"
    else:
        result = "Bad"
    return result
"""
import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
def main():
    """Get score and determine result based. Get random_score and determine random_result"""
    score = validate_score()
    result = determine_result(score)
    print(f"{score} - {result}")

    random_score = random.randint(0,100)
    random_result = determine_result(random_score)
    print(f"Grade of {random_score} is {random_result}")

def validate_score():
    """Get valid score"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def determine_result(score):
    """Determine result based on score"""
    if score >= EXCELLENT_THRESHOLD:
        result = "Excellent"
    elif score >= PASS_THRESHOLD:
        result = "Passable"
    else:
        result = "Bad"
    return result
main()