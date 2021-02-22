import string

char = input('Le caractère à crypter : ')
step = input('Le nombre de pas : ')
step = int(step)


letters = string.ascii_letters
letters = list(letters)
lenght = len(letters)

index = 0
code = ''

for letter in letters:
    if letter == char:
        index = letters.index(letter)
        break

position = index + step
rest = lenght - position

if rest < 0:
    position = rest + step - 1


code = letters[position]
print('Le caractère crypté est :', code)