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
    """The window class"""

    def __init__(self, title):
        """Create a new window and add a title"""
        Tk.__init__(self)
        self.title(title)

    def show(self):
        """Build and show the window"""
        return self.mainloop()