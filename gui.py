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



from tkinter import Tk, Label, Entry

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
        return Form()


class Form:
    """Create a new form from master"""
    
    fields: list = []

    def addField(self, pos: int):
        """Create a new field from form with pos as position"""
        field = FormField(self, pos)
        self.fields.append(field)
        return field


class FormField:
    """Create a new field from master with position"""

    form: Form
    pos: int = 0
    def __init__(self, form: Form, pos: int):
        self.form = form
        self.pos = pos

    def label(self, text: str, pos: int = 0):
        return FieldLabel(self, text, pos)

    def entry(self, pos: int = 1):
        return FieldEntry(self, pos)


class FieldLabel(Label):
    """Create a new field label from master with position and text"""

    field: FormField
    pos: int = 0
    fg: str = "#000"
    font: str = 'arial 18'
    anchor: str = 'w'
    padx: int = 15
    pady: int = 10
    sticky="nsew"
    
    def __init__(self, field: FormField, text: str, pos: int = 0):
        Label.__init__(self, text=text, fg=self.fg, font=self.font, anchor=self.anchor)
        self.field = field
        self.pos = pos

    def grid(self):
        return Label.grid(self, row=self.field.pos, column=self.pos, sticky=self.sticky)


class FieldEntry(Entry):
    """Create a new field entry from master with position and text"""

    field: FormField
    pos: int = 1
    fg: str = "#fff"
    font: str = 'arial 18'
    padx: int = 15
    pady: int = 10
    
    def __init__(self, field: FormField, pos: int = 1):
        Entry.__init__(self, fg=self.fg, font=self.font)
        self.field = field
        self.pos = pos

    def grid(self):
        return Entry.grid(self, row=self.field.pos, column=self.pos)