"""
Author: Han Su
Date: 18/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_08.unreliable_car import UnreliableCar


def main():
    """Test the unreliable car."""
    new_car = UnreliableCar("Toyota", 100, 80)
    another_car = UnreliableCar("Audi", 100, 20)

    for i in range(1, 11):
        print("Attempting to drive {}km:".format(i))
        print("{:8} drove {:2}km".format(new_car.name, new_car.drive(i)))
        print("{:8} drove {:2}km".format(another_car.name, another_car.drive(i)))

    print(new_car)
    print(another_car)


main()
