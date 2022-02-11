import os

#listing out all the contents of the directory and printing the list

dirList = os.listdir()
print(dirList)

#initializing list 
absPathList = []
#iterating through the list in the directory, joining the path to the filename
for file in dirList:
    pathName = r'C:\Users\mckay\OneDrive\Documents\GitHub\Python-Projects\Beginning Python Projects\scriptAssignment'
    absPath = os.path.join(pathName, file)
    #creating a new list with the absolute path
    absPathList.append(absPath)
    #printing to ensure things are looking good
print(absPathList)


txtList = []
#iterating through the absolute path list and creating a new list with those
    #files that end in .txt
for file in absPathList:
    #if file has the txt extension, they are added to a new list
    if file.endswith(".txt"):
        txtList.append(file)
    #if not, the iterating continues
    else:
        continue

#final iteration. Occurs on the new txt file list
for file in txtList:
    #here the file name is printed and then the last time it was
    #altered is also printed
    print(file)
    print(os.path.getmtime(file))
    


