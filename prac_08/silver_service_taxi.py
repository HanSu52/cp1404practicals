"""
Author: Han Su
Date: 18/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flag_fall + super().get_fare()

    def __str__(self):
        """Return a string like a Taxi and add flag-fall to it."""
        return "{} plus flag-fall of ${:.2f}".format(super().__str__(), self.flag_fall)
