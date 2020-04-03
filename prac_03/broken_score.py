"""
Author: Han Su
Date: 03/04/2020
https://github.com/HanSu52/cp1404practicals
"""


def main():
    """Grade determining program"""
    score = float(input("Enter score: "))
    get_grade(score)
    print(get_grade(score))


def get_grade(score):
    """Get the matched grade of the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif 90 <= score <= 100:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
