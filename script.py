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
word_label = word_field.setLabel('Tip the secret word :')
word_entry = word_field.setEntry()
word_field.grid()


step_field = form.addField(1)
step_label = step_field.setLabel('Tip the step number :')
step_entry = step_field.setEntry()
step_field.grid()

win.show()