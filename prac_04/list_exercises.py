"""
Author: Han Su
Date: 23/04/2020
https://github.com/HanSu52/cp1404practicals
"""


def main():
    get_numbers()


def get_numbers():
    numbers = []

    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is {}".format(numbers[0]))
    print("The last number is ".format(numbers[4]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is", sum(numbers)/len(numbers))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter the username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == '__main__':
    main()
