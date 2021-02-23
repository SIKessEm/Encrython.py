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

from crypter import encrypt, decrypt


label_fg = "#000"
label_font = 'arial 18'

entry_bg = "#fff"
entry_font = 'arial 22'
entry_place_y = 2

button_w = 10
button_h = 1
button_font = 'arial 16'


window = tkinter.Tk()
window.title("Encryption")
#window.geometry('300x200')
window.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)


word_field_label = tkinter.Label(
    master=window,
    text="Tip the secret word :",
    fg=label_fg,
    font=label_font
)
word_field_label.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=15,
    pady=10
)

word_field_entry = tkinter.Entry(
    master=window,
    bg=entry_bg,
    font=entry_font
)
word_field_entry.grid(
    row=0,
    column=1,
    padx=15,
    pady=10
)

step_field_label = tkinter.Label(
    master=window,
    text="Tip the step number : ",
    fg=label_fg,
    font=label_font
)
step_field_label.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=15,
    pady=10
)

step_field_entry = tkinter.Entry(
    master=window,
    bg=entry_bg,
    font=entry_font
)
step_field_entry.grid(
    row=1,
    column=1,
    padx=15,
    pady=10
)

result_label = tkinter.Label(master=window)

def encrypt_data():
    word = word_field_entry.get()
    step = int(step_field_entry.get())
    result_label['text'] = 'The encrypted code is "' + encrypt(word, step) + '"'

def decrypt_data():
    word = word_field_entry.get()
    step = int(step_field_entry.get())
    result_label['text'] = 'The decrypted code is "' + decrypt(word, step) + '"'

encrypt_button_frame = tkinter.Frame(
    master=window,
    relief=tkinter.RAISED,
    bd=2,
    bg='blue'
)
encrypt_button_frame.grid(
    row=2,
    column=0,
    padx=15,
    pady=10
)

encrypt_button = tkinter.Button(
    master=encrypt_button_frame,
    text='Encryt',
    bg="#0078ff",
    width=button_w,
    height=button_h,
    font=button_font,
    command=encrypt_data
)
encrypt_button.pack()

decrypt_button_frame = tkinter.Frame(
    master=window,
    relief=tkinter.RAISED,
    bd=2,
    bg='green'
)
decrypt_button_frame.grid(
    row=2,
    column=1,
    padx=15,
    pady=10
)

decrypt_button = tkinter.Button(
    master=decrypt_button_frame,
    text='Decryt',
    bg="#00ff78",
    width=button_w,
    height=button_h,
    font=button_font,
    command=decrypt_data
)
decrypt_button.pack()


result_label.grid(row=3, columnspan=2, padx=5, pady=10, sticky="nsew")


window.mainloop()