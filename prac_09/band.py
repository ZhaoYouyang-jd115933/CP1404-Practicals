class Band:
    """Class to represent a band, containing a collection of musicians."""
    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []
    def __str__(self):
        """Return a string representation of the band, including the name and the list of musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to band"""
        self.musicians.append(musician)

    def play(self):
        """Return a string of all musicians playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)
