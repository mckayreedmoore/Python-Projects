
#importing necessary libraries
from tkinter import *
import tkinter as tk
import webbrowser


#defining page creation function
def pageCreate():
    bodyText = tk.StringVar()
    
    bodyText = text1.get("1.0", END)
    
    # if the file already exists, it is overwritten
    fileA = open ('index.html','w')

    fileA.write(" \
            <html> \
               <body> \
                     <h1> \
                        " + bodyText + \
                    "<h1> \
                </body> \
            </html> \
            ")
    fileA.close()
    #opening freshly created webpage
    pageOpen('index.html')

    #opens webpage
def pageOpen(fileName):
    webbrowser.open_new_tab(fileName)

#creating tkinter python interface
win = tk.Tk()
win.Title = "Create Webpage"

text1 = tk.Text(win)
text1.grid(column=0, row=0, rowspan=3)

btn1 = tk.Button(win, text="Generate webpage", command = lambda: pageCreate())
btn1.grid(column=0, row=2)


