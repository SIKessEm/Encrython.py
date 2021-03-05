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

word_field = form.field(0)
word_label = word_field.label("Label")
word_entry = word_field.entry()

word_label.grid()
word_entry.grid()

win.show()