from random import randint as rand
from pyperclip import copy
import requests

# Asks the user how many characters long they would like their password.
length = input('How long would you like the password to be? - ')

# Continues to ask the user for a number until they enter a number.
while not int(length):
    length = input('How long would you like the password to be?')

# All the possible characters used to create the password.
possLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
possNumber = ['1','2','3','4','5','6','7','8','9','0']
possSymbol = ['!','"','£','$','%','^','&','*','(',')','@','+','_','-','=']

# Starting index of the password
i = 0

# Empty array, used to store the characters.
password = []

# Algorithm to generate random characters.
while i < int(length):

    # Variable used to determine the type of character.
    possRand = rand(1,4)

    # 50% chance of the character being a letter.
    if possRand in (1,2):

        # Defining the new character for this iteration.
        newDigit = possLetter[rand(0, possLetter.__len__()-1)]

        # 50% chance of the letter being upper-case.
        if rand(1,2) == 2:

            # Changing the character to upper-case.
            newDigit = newDigit.upper()

    # 25% chance of the character being a number.
    elif possRand == 3:

        # Defining the new character for this iteration.
        newDigit = possNumber[rand(0, possNumber.__len__()-1)]

    # 25% chance of the character being a symbol.
    elif possRand == 4:

        # Defining the new character for this iteration.
        newDigit = possSymbol[rand(0, possNumber.__len__()-1)]

    # Adding the new character to the array.
    password.append(newDigit)

    # Next letter.
    i += 1

# Copy the password to the clipboard.
copy(''.join(password))

print('')
# Outputs the pssword to the terminal window.
print(''.join(password))
print('')
print('The password has been copied to your clipboard.')
print('')
# Close the window.
input('Press Enter to Continue.')