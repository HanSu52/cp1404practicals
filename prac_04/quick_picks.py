"""
Author: Han Su
Date: 23/04/2020
https://github.com/HanSu52/cp1404practicals
"""


def main():
    import random
    PICKS_PER_LINE = 6
    number_of_picks = int(input("How many quick picks: "))

    for i in range(number_of_picks):
        quick_picks = []
        for pick in range(PICKS_PER_LINE):
            pick = random.randint(1, 45)
            while pick in quick_picks:
                pick = random.randint(1, 45)
            quick_picks.append(pick)
        quick_picks.sort()
        print(" ".join(repr(e) for e in quick_picks))


if __name__ == '__main__':
    main()
