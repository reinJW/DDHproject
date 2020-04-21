'''fileDia.py

module of methods that returns path and filename for user selected open or save  file
from filedialog ...

14-04-2020 imported and methods run in DDHmain

It needs tobe expanded ... to access more tkinter methods 

'''

import tkinter as tk
from tkinter import filedialog as fd

def conString(astring):
    return astring.replace('/','\\\\')

def saveFile():
    window = tk.Tk()
    window.withdraw()
    sfileString = conString(fd.asksaveasfilename())
    return sfileString

def openFile():
    window = tk.Tk()
    window.withdraw()
    ofileString = conString(fd.askopenfilename())
    return ofileString

