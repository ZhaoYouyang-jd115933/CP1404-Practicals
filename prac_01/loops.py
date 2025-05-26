"""
repeat odd number i from 1 to 21
    display i
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
"""
repeat multiples of 10 from 0 to 110
      display number
"""
for number in range(0, 110, 10):
    print(number, end=" ")
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
"""
repeat number from 20 to 0
     display number
"""
for number in range(20, 0, -1):
    print(number, end=" ")
print()

# c. print n stars. Ask the user for a number, then print that many stars (*), all on one line.
"""
get number_of_stars
display "*" * number_of_stars
"""
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

# d. print n lines of increasing stars.
"""
get number_of_stars
repeat star for number of stars times
     display "*" * star
"""
number_of_stars = int(input("Number of stars: "))
for star in range(1, number_of_stars+1):
    print("*" * star)