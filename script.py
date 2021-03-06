#-------------------------------------------------------------------------------
# Name:        sikessem-encryption
# Purpose:
#
# Author:      SIGUI Kessé Emmanuel
#
# Created:     05/03/2021
# Copyright:   (c) SIKessEm 2021
# Licence:     MIT
#-------------------------------------------------------------------------------



from gui import Window, Form


window = Window('Encryption')

form = window.addForm()
form.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
form.columnconfigure([0, 1], minsize=50, weight=1)

word_field = form.addField(0)
word_label = word_field.setLabel('Tip the secret word :')
word_entry = word_field.setEntry()
word_label.grid()
word_entry.grid()
word_field.pack()


step_field = form.addField(1)
step_label = step_field.setLabel('Tip the step number :')
step_entry = step_field.setEntry()
step_label.grid()
step_entry.grid()
step_field.pack()


encrypt_block = form.addBlock()
encrypt_block.grid(row=2, column=0)
encrypt_button = encrypt_block.addButton('Encrypt')
encrypt_button.pack()


decrypt_block = form.addBlock()
decrypt_block.grid(row=2, column=1)
decrypt_button = decrypt_block.addButton('Decrypt')
decrypt_button.pack()


form.pack()

window.loop()