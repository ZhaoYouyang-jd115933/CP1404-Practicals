"""
CP1404/CP5632 - Practical
Broken program to determine score status

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

get score
while score less than 0 or score greater than 100
    display "Invalid score"
    get score
if score > 50
    display "Passable"
else if score > 90
    display "Excellent"
else
    display "Bad"
"""

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