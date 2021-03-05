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


win = Window('Encryption')

form = win.form()

word_field = form.addField(0)
word_label = word_field.label('Tip the secret word :')
word_entry = word_field.entry()

word_label.grid()
word_entry.grid()


step_field = form.addField(1)
step_label = step_field.label('Tip the step number : ')
step_entry = step_field.entry()

step_label.grid()
step_entry.grid()

win.show()