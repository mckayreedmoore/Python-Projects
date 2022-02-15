import shutil
import os
import time
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile



#needs of program
    #gather metadata about when the file was created
        #create list of this metadata
    #gather metadata about when the file was modified
        #create list of this metadata
    #determine if file has been created for modifed/created
        #iterate through list comparing modified time
        #with current time. If the modifed time occurred
        #within last 24 hours, add it to the list of
        #modified files.
    #send modifed files to folder that will copy them
    #at the end of the day



folderAbsPathList = []

def fileSearchAndMove():
    #getting source and destination folders for file transfer
    source = text1.get()
    
    destination = text2.get()

    folderPath = source
    
    #lists all the files in the source folder and creates a list
    #of the absolute path file names
    dirList = os.listdir(folderPath)

    for file in dirList:
        completeFileName = os.path.join(folderPath, file)
        folderAbsPathList.append(completeFileName)
    print(folderAbsPathList)
    #function recieves time last modified and returns time since
    #since modification
    def checkTime(timeModified):
        currentTime = time.time()
        timeFromMod = currentTime - timeModified
        return timeFromMod

    #gets the time since last modification and compares it with the epoch
    #time. If the file has been modified in the last 24 hours, it is moved
    #to the folder with all the modified files
    moveList = []

    i = 0
    while i < len(folderAbsPathList):
        print(os.path.getmtime(folderAbsPathList[i]))
        timeModified = os.path.getmtime(folderAbsPathList[i])
        #if the file was modified in the last 24 hours,
        #move it to a  moveList
        if checkTime(timeModified) < 86400:
            moveList.append(folderAbsPathList[i])
        i = 1 + i
    for absFilePath in moveList:
            shutil.move(absFilePath,destination)




win = Tk()

#initializing text variable
textbox1 = StringVar()

#initializing text variable
textbox2 = StringVar()

#text fields
text1 = Entry(win, textvariable=textbox1)
text1.grid(row=1, column=1, columnspan=3)
text2 = Entry(win, textvariable=textbox2)
text2.grid(row=2, column=1, columnspan=3)

#declaring functions
def selectInitDir():
    file = filedialog.askdirectory()
    path = os.path.abspath(file)
    textbox1.set(path)
    print(file)
    print(path)

def selectFinalDir():
    file = filedialog.askdirectory()
    path = os.path.abspath(file)
    textbox2.set(path)
    print(file)
    print(path)
   
    

#empty row at top
lb1 = Label(win, text='  \n  ')
lb1.grid(column=0, row=0, columnspan=4)

#empty section middle bottom
lb2 = Label(win, text='  \n  ')
lb2.grid(column=1, row=3, columnspan=3, padx=(30,30))

#buttons
btn1 = Button(win, text='Select Initial Directory', command= lambda: selectInitDir() )
btn1.grid(row=1, column=0, padx=(30,30), pady=(10,10))
btn2 = Button(win, text='Select Final Directory', command= lambda: selectFinalDir())
btn2.grid(row=2, column=0, padx=(30,30), pady=(10,10))
btn3 = Button(win, text='Run Operation', command= lambda: fileSearchAndMove())
btn3.grid(row=3, column=0, padx=(30,30), pady=(40,40))
btn4 = Button(win, text='CloseProgram', command= lambda: win.destory())
btn4.grid(row=3, column=3, padx=(30,30), pady=(40,40))
    
        

    



    
