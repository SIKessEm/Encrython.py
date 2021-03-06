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



from tkinter import Tk, Frame, Label, Entry, Checkbutton, Radiobutton, Listbox

__all__ = [
    'Window',
    'Form',
    'FormField',
    'FieldEntry',
    'FieldLabel',
    'FormOptions',
    'FieldRadio',
    'FieldSelect',
    'FieldCheckbox',
    'FormButton',
    'ButtonSubmit',
    'ButtonReset',
    'ButtonCancel'
]

class Window(Tk):
    """Create a new window and add a title"""

    def __init__(self, title, **kw):
        super().__init__(**kw)
        self.title(title)

    def loop(self):
        """Launch the window"""
        return self.mainloop()
    
    def addForm(self, **kw):
        """Create a new form"""
        form = Form(self, **kw)
        return form


class Form(Frame):
    """Create a new form from master"""

    fields: list = []

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

    def addField(self, pos: int):
        """Create a new field from form with pos as position"""
        field = FormField(self, pos)
        self.fields.append(field)
        return field


class FormField(Frame):
    """Create a new field from master with position"""

    form: Form
    pos: int = 0
    def __init__(self, form: Form, pos: int, **kw):
        super().__init__(form, **kw)
        self.form = form
        self.pos = pos

    def setLabel(self, text: str, pos: int = 0, **kw):
        self.label = FieldLabel(self, text, pos, **kw)
        return self.label

    def setEntry(self, pos: int = 1, **kw):
        self.input = FieldEntry(self, pos, **kw)
        return self.input

    def setRadio(self, pos: int = 1, **kw):
        self.input = FieldRadio(self, pos, **kw)
        return self.input


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
    
    def __init__(self, field: FormField, text: str, pos: int = 0, **kw):
        super().__init__(field, text=text, fg=self.fg, font=self.font, anchor=self.anchor, **kw)
        self.field = field
        self.pos = pos

    def grid(self, **kw):
        return super().grid(row=self.field.pos, column=self.pos, sticky=self.sticky, **kw)


class FieldEntry(Entry):
    """Create a new field entry from master with position and text"""

    field: FormField
    pos: int = 1
    fg: str = "#fff"
    font: str = 'arial 18'
    padx: int = 15
    pady: int = 10
    
    def __init__(self, field: FormField, pos: int = 1, **kw):
        super().__init__(field, fg=self.fg, font=self.font, **kw)
        self.field = field
        self.pos = pos

    def grid(self, **kw):
        return super().grid(row=self.field.pos, column=self.pos, **kw)


class FieldRadio(Radiobutton):
    """Create a new field radio from master with position and text"""

    field: FormField
    pos: int = 1
    font: str = 'arial 18'
    padx: int = 15
    pady: int = 10
    
    def __init__(self, field: FormField, pos: int = 1, **kw):
        super().__init__(field, font=self.font, **kw)
        self.field = field
        self.pos = pos

    def grid(self, **kw):
        return super().grid(row=self.field.pos, column=self.pos, **kw)