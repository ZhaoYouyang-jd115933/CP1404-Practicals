"""
Project class
Estimate: 1 hours
Actual:  50 minutes
"""

import datetime
class Project:
    """Represent a Project object"""

    def __init__(self, name, date, priority = 0, cost = 0, completion_percentage = 0):
        """Initialise a Project instance"""
        self.name = name
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def is_complete(self):
        """Check whether completion percentage is equal to 100"""
        return self.completion_percentage == 100

    def __str__(self):
        """Convert string for output"""
        return f"{self.name}, start: {self.date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion_percentage}%"

    def change_string(self):
        """Set up the format of write file method."""
        return f"{self.name}\t{self.date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost}\t{self.completion_percentage}"