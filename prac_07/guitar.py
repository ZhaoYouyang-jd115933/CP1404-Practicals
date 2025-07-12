class Guitar:
    """Represent a Guitar object"""
    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Convert object to string"""
        return f"{self.name} L-5 CES ({self.year}) : {self.cost}"

    def __lt__(self, other):
        """Compare guitars with year"""
        return self.year < other.year