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



from tkinter import *

__all__ = [
    'Window',
    'Form',
    'FormField',
    'FieldEntry',
    'FieldLabel',
    'FieldRadio',
    'FieldSelect',
    'FieldCheckbox',
    'FormBlock',
    'FormButton'
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

    childs: list = []

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master

    def addField(self, pos: int, **kw):
        """Create a new field from form with pos as position"""
        field = FormField(self.master, pos, **kw)
        self.childs.append(field)
        return field
    
    def addBlock(self, **kw):
        """Create a new block from form with pos as position"""
        block = FormBlock(self.master, **kw)
        self.childs.append(block)
        return block


class FormBlock(Frame):
    """Create a new Block from master with position"""

    form: Form
    relief=RAISED
    bd=2
    padx=15
    pady=10

    def __init__(self, form: Form, **kw):
        super().__init__(form, relief=self.relief, bd=self.bd, **kw)
        self.form = form

    def addButton(self, text: str, pos: int = 0, **kw):
        self.button = FormButton(self, **kw)
        return self.button

    def grid(self, **kw):
        super().grid(padx=self.padx, pady=self.pady, **kw)


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

    def setSelect(self, pos: int = 1, **kw):
        self.input = FieldSelect(self, pos, **kw)
        return self.input

    def setCheckbox(self, pos: int = 1, **kw):
        self.input = FieldCheckbox(self, pos, **kw)
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
    
    def __init__(self, field: FormField, pos: int = 1, **kw):
        super().__init__(field, **kw)
        self.field = field
        self.pos = pos

    def grid(self, **kw):
        return super().grid(row=self.field.pos, column=self.pos, **kw)


class FieldSelect(Listbox):
    """Create a new field select from master with position and text"""

    field: FormField
    pos: int = 1
    
    def __init__(self, field: FormField, pos: int = 1, **kw):
        super().__init__(field, **kw)
        self.field = field
        self.pos = pos

    def grid(self, **kw):
        return super().grid(row=self.field.pos, column=self.pos, **kw)


class FieldCheckbox(Checkbutton):
    """Create a new field check from master with position and text"""

    field: FormField
    pos: int = 1
    
    def __init__(self, field: FormField, pos: int = 1, **kw):
        super().__init__(field, **kw)
        self.field = field
        self.pos = pos

    def grid(self, **kw):
        return super().grid(row=self.field.pos, column=self.pos, **kw)


class FormButton(Button):
    """Create a new block button from master with position and text"""

    block: FormBlock
    width = 10
    height = 1
    font ='Arial 16'
    
    def __init__(self, block: FormBlock, **kw):
        super().__init__(master=block, width=self.width, height=self.height, font=self.font, **kw)
        self.block = block

    def pack(self, **kw):
        return super().pack(**kw)