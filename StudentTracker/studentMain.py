# Author - > McKay Reed Moore

# Program contents - > This program is a sort of student tracker

# Purpose - > this is the be able to refine my skills in python and
    #associated technologies


import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import messagebox



import studentFUNC
import studentGUI




#a page labeled student tracking
#form fields - first name, last name, phone number, email, current course,
    #submit button
#section that displays the list of all students with the relevant information
#a delete button


class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        # this CenterWindow method will center the app on the user's screen
        studentFUNC.center_window(self,500,300)
        self.master.title('Student Tracking')
        self.master.configure(bg='#f0f0f0')


        #loads in GUI
        studentGUI.load_gui(self)

        



if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
