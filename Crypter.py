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




code = decrypt(word, step)

print('Le mot crypté est :', code)