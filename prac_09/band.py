class Band:
    """Class to represent a band, containing a collection of musicians."""
    def __init__(self, name=""):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = []
    def __str__(self):
        """Return a string representation of the band, including the name and the list of musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
