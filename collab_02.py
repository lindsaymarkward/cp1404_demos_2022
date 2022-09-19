"""
Write a program that asks the user for a low and high number,
ensuring the high is higher than the low.
Then print n smiley faces, where n is a random number between
low and high inclusive.
"""

# import random  # way 1
from random import randint  # 2

SMILEY = ":) "


def main():
    """Program to print random smileys."""
    low = int(input("Low: "))
    high = int(input("High: "))
    while high <= low:
        print(f"High must be > {low}")
        high = int(input("High: "))
    # comment
    number_of_smileys = randint(low, high)
    print(number_of_smileys)
    print(number_of_smileys * SMILEY)


main()
