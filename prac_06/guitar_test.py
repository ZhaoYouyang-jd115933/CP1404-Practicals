"""
Word Occurrences
Estimate: 10 minutes
Actual:   10 minutes
"""
from prac_06.guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Line 6 JTV-59", 2013, 1512.9)
print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")