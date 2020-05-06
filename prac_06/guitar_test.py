"""
Author: Han Su
Date: 01/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922)
    another_guitar = Guitar("Another Guitar", 2013)
    print(gibson.get_age())
    print(another_guitar.get_age())
    print(gibson.is_vintage())
    print(another_guitar.is_vintage())


main()
