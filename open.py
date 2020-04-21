'''Creates a simple window with a file open button '''


import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
tk.Button(text='File Open', 
       command=callback).pack(fill=tk.X)
tk.mainloop()
