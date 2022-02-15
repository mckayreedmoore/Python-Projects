import shutil
import os

#source of files
source = r"C:\Users\mckay\OneDrive\Documents\GitHub\Python-Projects\file-transfer-assignment\FolderA\\"

#destination of files
destination = r"C:\Users\mckay\OneDrive\Documents\GitHub\Python-Projects\file-transfer-assignment\FolderB\\"

#creates a list of files in our source folder
files = os.listdir(source)

#iterates through the list of files in source folder and moves them
for i in files:
    shutil.move(source+i,destination)
        
    
