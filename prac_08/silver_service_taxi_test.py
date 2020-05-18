"""
Author: Han Su
Date: 18/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxis class"""
    new_taxi = SilverServiceTaxi("Silver", 100, 2)
    new_taxi.drive(18)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
