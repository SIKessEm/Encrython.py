#-------------------------------------------------------------------------------
# Name:        sikessem-gui
# Purpose:
#
# Author:      SIGUI Kessé Emmanuel
#
# Created:     05/03/2021
# Copyright:   (c) SIKessEm 2021
# Licence:     MIT
#-------------------------------------------------------------------------------



from tkinter import Tk, Label

class Window(Tk):
    """Create a new window and add a title"""

    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)

    def show(self):
        """Build and show the window"""
        return self.mainloop()
    
    def form(self):
        """Create a new form"""
        return Form(self)


class Form:
    """Create a new form from master"""

    def __init__(self, *master):
        self.master = master
    
    def field(self, pos: int):
        """Create a new field from form with pos as position"""
        return Field(pos, self.master)


class Field:
    """Create a new field from master with position"""

    label: Label
    label_fg = "#000"
    label_font = 'arial 18'
    label_anchor = 'w'

    pos: int = 0
    def __init__(self, pos: int, *master):
        self.pos = pos
        self.master = master

    def label(self, pos: int, text: str):
        return self.label = Label(
            master=self.master,
            text=text,
            fg=self.label_fg,
            font=self.label_font,
            anchor=self.label_anchor
        )