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

    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)