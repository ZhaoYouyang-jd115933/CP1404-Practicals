"""
CP1404/CP5632 - Practical
Broken program to determine score status

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

get score
while score less than MINIMUM_SCORE or score greater than MAXIMUM_SCORE
    display "Invalid score"
    get score
if score > EXCELLENT_THRESHOLD
    display "Excellent"
else if score > PASS_THRESHOLD
    display "Passable"
else
    display "Bad"
"""

# TODO: Fix this!

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
score = float(input("Enter score: "))
while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid score")
    score = float(input("Enter score: "))
if score > EXCELLENT_THRESHOLD:
    print("Excellent")
elif score > PASS_THRESHOLD:
    print("Passable")
else:
    print("Bad")