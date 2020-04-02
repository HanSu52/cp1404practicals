def main():
    import random
    print(random.randint(5, 20))  # line 1
    """What did you see on line 1?
       An integer between 5 to 20(20 not included).
       What was the smallest number you could have seen, what was the largest?
       The smallest is 5, and the largest is 19.
    """
    print(random.randrange(3, 10, 2))  # line 2
    """What did you see on line 2?
       An odd integer between 3 to 10.
       What was the smallest number you could have seen, what was the largest?
       The smallest is 3, and the largest is 9.
       Could line 2 have produced a 4?
       No.
    """
    print(random.uniform(2.5, 5.5))  # line 3
    """What did you see on line 3?
       A real number between 2.5 to 5.5(5.5 not included).
       What was the smallest number you could have seen, what was the largest?
       Thee smallest is 2.5, and largest number is going to be infinitely close to 5.5.
    """
    print(random.randrange(1, 101))


if __name__ == '__main__':
    main()
