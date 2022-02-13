
from tkinter import *

win = Tk()

win.title('Check Files')

#empty row at top
lb1 = Label(win, text='  \n  ')
lb1.grid(column=0, row=0, columnspan=4)

#empty section middle bottom
lb2 = Label(win, text='  \n  ')
lb2.grid(column=1, row=3, columnspan=3, padx=(30,30))

#buttons
btn1 = Button(win, text='Browse...')
btn1.grid(row=1, column=0, padx=(30,30), pady=(10,10))
btn2 = Button(win, text='Browse...')
btn2.grid(row=2, column=0, padx=(30,30), pady=(10,10))
btn3 = Button(win, text='Check for files...')
btn3.grid(row=3, column=0, padx=(30,30), pady=(40,40))
btn4 = Button(win, text='CloseProgram')
btn4.grid(row=3, column=3, padx=(30,30), pady=(40,40))


#text fields
text1 = Entry(win)
text1.grid(row=1, column=1, columnspan=3)
text2 = Entry(win)
text2.grid(row=2, column=1, columnspan=3)

