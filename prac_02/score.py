"""
CP1404/CP5632 - Practical
Broken program to determine score status

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

function main()
    score = validate_score()
    if score > EXCELLENT_THRESHOLD
        display "Excellent"
    else if score > PASS_THRESHOLD
        display "Passable"
    else
        display "Bad"

function validate_score()
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE
        display "Invalid score"
        score = float(input("Enter score: "))
    return score
"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
def main():
    score = validate_score()
    if score > EXCELLENT_THRESHOLD:
        print("Excellent")
    elif score > PASS_THRESHOLD:
        print("Passable")
    else:
        print("Bad")

def validate_score():
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score
main()