from random import randint as rand
from pyperclip import copy
import requests
import argparse

parser = argparse.ArgumentParser(description='Generate a strong password.')
parser.add_argument('-l', '--length', type=int, action='store', dest='length', default=15, help='Length of the password (default=15).')
parser.add_argument('-c', '--clipboard', action='store_true', dest='clipboard', help='Copy the password to clipboard.')

args = parser.parse_args()

def generate_password(length: int = 15, clipboard: bool = False):

    # All the possible characters used to create the password.
    possLetter = 'abcdefghijklmnopqrstuvwxyz'
    checkLetter = False
    checkLetterUpper = False
    possNumber = '0123456789'
    checkNumber = False
    possSymbol = r'!"£$%^&*()-_=+[]{}@~#,.<>/?|'
    checkSymbol = False

    if length < 8:
        return 'ERROR: Password cannot be shorter than 8 characters.'

    # Starting index of the password
    i = 0

    # Empty array, used to store the characters.
    password = []

    # Algorithm to generate random characters.
    while i < int(length):

        # Variable used to determine the type of character.
        possRand = rand(1,4)

        # 50% chance of the character being a letter.
        if possRand <= 2:

            # Defining the new character for this iteration.
            newDigit = possLetter[rand(0, possLetter.__len__() - 1)]
            checkLetter = True

            # 50% chance of the letter being upper-case.
            if rand(1,2) == 2:

                # Changing the character to upper-case.
                newDigit = newDigit.upper()
                checkLetterUpper = True

        # 25% chance of the character being a number.
        elif possRand == 3:

            # Defining the new character for this iteration.
            newDigit = possNumber[rand(0, possNumber.__len__() - 1)]
            checkNumber = True

        # 25% chance of the character being a symbol.
        elif possRand == 4:

            # Defining the new character for this iteration.
            newDigit = possSymbol[rand(0, possNumber.__len__() - 1)]
            checkSymbol = True

        # Adding the new character to the array.
        password.append(newDigit)

        # Next letter.
        i += 1

    if False in [checkLetter, checkLetterUpper, checkNumber, checkSymbol]:
        generate_password(length=length, clipboard=clipboard)

    password = ''.join(password)

    # Copy the password to the clipboard.
    if clipboard:
        copy(password)

    return password

if __name__ == '__main__':
    print(generate_password(length=args.length, clipboard=args.clipboard))
    input('')