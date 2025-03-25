#!/usr/bin/env python3
# Created By: Beni
# Date: March 23, 2025
# Check if a number is positive or negative

def main():

    print("I can tell you if your number is positive or negative")

    # Gets the users number
    number = float(input("What is your number?: "))

    # If you have a positive number
    if number > 0:
        print("{} is a positive number". format (number))

    # If you have a negative number
    elif number < 0:
        print("{} is a negative number". format(number))

    # If number isn't positive or negative
    else:
        print("You aren't slick buddy, your number is 0")

if __name__ == "__main__":
    main()
