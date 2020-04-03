"""
Author: Han Su
Date: 03/04/2020
https://github.com/HanSu52/cp1404practicals
"""

MENU = """C - Convert Celsius to Fahrenheit
          F - Convert Fahrenheit to Celsius
          Q - Quit"""


def main():
    """Temperature conversion program"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_to_fahrenheit(celsius)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_to_celsius(fahrenheit)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit):
    """Convert the given Fahrenheit degrees to Celsius degrees."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return "Result: {:.2f} C".format(celsius)


def convert_to_fahrenheit(celsius):
    """Convert the given Celsius degrees to Fahrenheit degrees."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return "Result: {:.2f} F".format(fahrenheit)


if __name__ == '__main__':
    main()
