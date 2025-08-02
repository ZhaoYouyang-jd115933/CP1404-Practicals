import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability and new drive method."""
    def __init__(self, reliability, **kwargs):
        """Initialise an UnreliableCar instance."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability chance."""
        percentage_chance = random.uniform(0, 100)
        if percentage_chance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven


