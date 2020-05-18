"""
Author: Han Su
Date: 18/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_08.taxi import Taxi


def main():
    """Test the Taxi class"""
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    print(new_taxi.get_fare())

    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
