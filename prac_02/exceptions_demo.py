"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   When the input number of either the numerator or the denominator is not an integer.
2. When will a ZeroDivisionError occur?
   When the input number of the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)
    print("Finished")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
