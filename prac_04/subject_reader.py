"""
Author: Han Su
Date: 23/04/2020
https://github.com/HanSu52/cp1404practicals
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_subject(data):
    """Display all the subjects."""
    for subjects in data:
        print("{} is taught by {} and has {} students".format(*subjects))


if __name__ == '__main__':
    main()
