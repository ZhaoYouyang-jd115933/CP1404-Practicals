import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# It prints all the integers between 5 and 20
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5 and the largest number is 20

# What did you see on line 2?
# The result of this random function is 3, 5, 7, 9
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3 and the largest number is 9
# Could line 2 have produced a 4?
# Line 2 could not have produced a 4. This is because step is 2 and start from 3, so it only print odd numbers

# What did you see on line 3?
# It prints any float between 2.5 and 5.5, such as 2.7785295157992067, 3.5186683110679136
# What was the smallest number you could have seen, what was the largest?
# The smallest number is close to 2.5, but it can not be exactly 2.5
# The largest number is close to 5.5, but it can not be exactly 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
import random
random_number = random.randint(1, 100)
print(random_number)



