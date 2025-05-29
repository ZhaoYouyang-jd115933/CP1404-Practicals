"""
CP1404/CP5632 - Practical
Broken program to determine score status

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

# TODO: Fix this!

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score > 50:
    print("Passable")
elif score > 90:
    print("Excellent")
else:
    print("Bad")