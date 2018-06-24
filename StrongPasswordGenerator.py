from random import randint as rand
from pyperclip import copy

# Asks the user how many characters long they would like their password.
length = input('How long would you like the password to be? - ')

# Continues to ask the user for a number until they enter a number.
while not int(length):
    length = input('How long would you like the password to be?')

# All the possible characters used to create the password.
possLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
possNumber = ['1','2','3','4','5','6','7','8','9','0']
possSymbol = ['!','"','£','$','%','^','&','*','(',')','@','+','_','-','=']

i = 0 				# Starting index of the password
password = []		# Empty array, used to store the characters.

# Algorithm to generate random characters.
while i < int(length):

    possRand = rand(1,4) 											# Variable used to determine the type of character.

    if possRand in (1,2): 											# 50% chance of the character being a letter.

        newDigit = possLetter[rand(0, possLetter.__len__()-1)]		# Defining the new character for this iteration.

        if rand(1,2) == 2: 											# 50% chance of the letter being upper-case.

            newDigit = newDigit.upper()								# Changing the character to upper-case.

    elif possRand == 3:												# 25% chance of the character being a number.

        newDigit = possNumber[rand(0, possNumber.__len__()-1)]		# Defining the new character for this iteration.

    elif possRand == 4:												# 25% chance of the character being a symbol.

        newDigit = possSymbol[rand(0, possNumber.__len__()-1)]		# Defining the new character for this iteration.

    password.append(newDigit)										# Adding the new character to the array.

    i += 1															# Next letter.

copy(''.join(password))												# Copy the password to the clipboard.

print('')
print(''.join(password))											# Outputs the pssword to the terminal window.
print('')
print('The password has been copied to your clipboard.')
print('')
input('Press Enter to Continue.')									# Close the window.