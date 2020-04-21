#! tkopenfile.py

''' demos how you might be able to use the openfiledialog to get a path\filename 
in a windows compatible format ... '''

import tkinter as tk
from tkinter import filedialog as fd

def conFileString(astring):
    return astring.replace('/','\\\\')

def findFile():
    window = tk.Tk()
    window.withdraw() # withdraws GUI - no window
    openFilePath = fd.askopenfilename()
    return openFilePath

print(findFile())





