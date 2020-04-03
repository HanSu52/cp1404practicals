"""
Author: Han Su
Date: 03/04/2020
https://github.com/HanSu52/cp1404practicals
"""
MINIMUM_LENGTH = 6


def main():
    """A program that asks the user for a password and prints asterisks based on its length."""
    password = get_password(MINIMUM_LENGTH)
    get_asterisks(password)


def get_password(minimum_length):
    """Get a valid password with at least 6 characters."""
    password = input("Please enter a valid password with at least {} characters: ".format(minimum_length))
    while len(password) < MINIMUM_LENGTH:
        print("Your password is invalid.")
        password = input("Please enter a valid password with at least 6 characters: ".format(minimum_length))
    return password


def get_asterisks(password):
    """Print as many asterisks as the length of the given password."""
    print(len(password) * "*")


if __name__ == '__main__':
    main()
