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



from crypter import encrypt, decrypt

print('>>>BIENVENUE DANS NOTRE PROGRAMME DE CRYPTAGE<<<')
print('-------------------------------------------------')

word = input('Le mot à crypter : ')

step = input('Le nombre de pas : ')

step = int(step)

action = ''

while action not in ['-', '+', 'e', 'd']:

    action = input('Encrypter (+|e) ou Décrypter (-|d) ? ')

else:

    if action in ['-', 'd']:

        code = decrypt(word, step)

    else:

        code = encrypt(word, step)



print('Le mot crypté est :', code)
print('-------------------------------------------------')
input("===Tapez sur n'importe quel touche pour sortir===")