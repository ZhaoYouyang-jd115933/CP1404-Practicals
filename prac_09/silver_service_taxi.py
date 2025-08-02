from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A fancier version of Taxi with a flagfall charge."""
    flag_fall = 4.50
    def __init__(self, fanciness, **kwargs):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flag_fall:.2f}"

    def get_fare(self):
        """Return the price add flag fall for the silver taxi trip."""
        return super().get_fare() + self.flag_fall


