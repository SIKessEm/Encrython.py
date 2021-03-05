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



from tkinter import Tk

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

