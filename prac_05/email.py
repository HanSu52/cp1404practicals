"""
Author: Han Su
Date: 24/04/2020
https://github.com/HanSu52/cp1404practicals
"""


def main():
    name_and_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        verify = input("Is your name {}? (Y/n)".format(name)).upper()
        if verify != "Y":
            name = input("Name: ")
        name_and_email[name] = email
        email = input("Email: ")

    for name, email in name_and_email.items():
        print("{} ({})".format(name, email))


def get_name(email):
    user_name = email.split('@')[0]
    separate_name = user_name.split('.')
    name = " ".join(separate_name).title()
    return name


if __name__ == '__main__':
    main()
