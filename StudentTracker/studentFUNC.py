
import os
from tkinter import *
import tkinter as tk
import sqlite3




import studentMain
import studentGUI



def center_window(self, w, h):

    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        #This closes app
        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_student(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_cclass TEXT \
            );')
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_student.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("INSERT INTO tbl_student (col_fname,col_lname,col_fullname,col_phone,col_email,col_cclass) \
                        VALUES (?,?,?,?,?,?)",('John','Doe','John Doe','111-111-1111','jdoe@email.com','Math'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ''
    cur.execute("""SELECT COUNT (*) FROM tbl_student""")
    count = cur.fetchone()[0]
    return cur,count

#ListBox item selection
def onSelect(self,event):
    #calling event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_cclass FROM tbl_student WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_cclass.delete(0,END)
            self.txt_cclass.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize data to keep what is in the database consistent
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ('{} {}'.format(var_fname,var_lname)) #creates var fullname
    print('var_fullname: {}'.format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_cclass = self.txt_cclass.get().strip()
    
    conn = sqlite3.connect('db_student.db')
    with conn:
        cursor = conn.cursor()
        #checks the database for existence of fullname.
            #If the name already exists, we will alert the user
        cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_student WHERE col_fullname = '{}'""".format(var_fullname))                                                                     
        count = cursor.fetchone()[0]
        chkName = count
        if chkName == 0:
            print("chkName: {}".format(chkName))
            cursor.execute("""INSERT INTO tbl_student (col_fname,col_lname,col_fullname,col_phone,col_email,col_cclass) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_cclass))
            self.lstList1.insert(END, var_fullname) # update listbox with the new fullname
            onClear(self) # call the function to clear all of the textboxes
        else:
            messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
            onClear(self) # call the function to clear all of the textboxes
        conn.commit()
    conn.close()
                                                                                
def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())
    conn = sqlite3.connect('db_student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM tbl_student WHERE col_fullname = '{}'""".format(var_select))
    onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
######             onRefresh(self) # update the listbox of the changes
    conn.commit()
    conn.close()

def onDeleted(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_cclass.delete(0,END)

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_cclass.delete(0,END)

def onRefresh(self):
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_student.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_student""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_student""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()




if __name__ == "__main__":
    pass


                      
                                                                                  
                                                                                  


















    
