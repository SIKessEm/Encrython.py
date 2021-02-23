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


import tkinter


label_fg = "#000"
label_h = 1
label_w = 40

entry_bg = "#fff"
entry_w = 60

button_w = 20
button_h = 2


window = tkinter.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)


word_field_label = tkinter.Label(
    master=window,
    text="The secret word : ",
    fg=label_fg
)
word_field_label.grid(row=0, column=0, sticky="nsew", padx=15, pady=10)

word_field_entry = tkinter.Entry(
    master=window,
    bg=entry_bg
)
word_field_entry.grid(row=0, column=1, padx=15, pady=10)




window.mainloop()