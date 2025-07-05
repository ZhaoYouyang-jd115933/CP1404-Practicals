"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""
CURRENT_YEAR = 2022
AGE_THRESHOLD = 50
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Convert object to string"""
        return f"{self.name} L-5 CES ({self.year}) : {self.cost}"

    def get_age(self):
        """Calculate how old the guitar is in years"""
        guitar_age = CURRENT_YEAR - self.year
        return guitar_age

    def is_vintage(self):
        """Check if the guitar is 50 or more years old"""
        guitar_age = self.get_age()
        if guitar_age >= AGE_THRESHOLD:
            return True
        else:
            return False

