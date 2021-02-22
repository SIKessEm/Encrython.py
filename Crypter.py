#-------------------------------------------------------------------------------
# Name:        sikessem-encryption
# Purpose:
#
# Author:      SIGUI Kessé Emmanuel
#
# Created:     18/02/2021
# Copyright:   (c) SIKessEm 2021
# Licence:     MIT
#-------------------------------------------------------------------------------



import string


word = input('Le mot à crypter : ')

step = input('Le nombre de pas : ')

step = int(step)


letters = string.ascii_letters

letters = list(letters)

lenght = len(letters)


def encrypt(word, step):

    code = ''

    word_letters = list(word)

    for word_letter in word_letters:

        index = 0

        for letter in letters:

            if letter == word_letter:

                index = letters.index(letter)

                break

        position = index + step

        rest = lenght - position

        if rest < 0:

            position = rest + step - 1

        code += letters[position]

    return code



def decrypt(word, step):

    code = ''

    word_letters = list(word)

    for word_letter in word_letters:

        index = 0

        for letter in letters:

            if letter == word_letter:

                index = letters.index(letter)

                break

        position = index - step

        if position < 0:

            position += lenght

        code += letters[position]

    return code


action = ''

while action not in ['-', '+', 'e', 'd']:

    action = input('Encrypter (+|e) ou Décrypter (-|d) ? ')

else:

    if action in ['-', 'd']:

        code = decrypt(word, step)

    else:

        code = encrypt(word, step)



print('Le mot crypté est :', code)