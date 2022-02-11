import sqlite3

#tuple containing file names
fileList=('information.docx','hello.txt','myImage.png', \
          'myMovie.mpg','world.txt','data.pdf','myPhoto.jpg')
#declare connection variable
conn = sqlite3.connect('mainDatabase.db')

#while you have a connection, execute this SQL
while conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data (\
        file_id INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()
conn.close()

#this initializes a list for storing txt file names in
txtList = []
#this iterates through our fileList tuple and creates a list
#having only .txt files in it
for file in fileList:
    if file.endswith('txt'):
        txtList.append(file)
    else:
        continue
print(txtList)

conn = sqlite3.connect('mainDatabase.db')
while conn:
    #this inserts all items from txtList into our database
    for i in txtList:
        cur.execute('INSERT INTO tbl_data (col_file)\
            VALUE (?)'.format(i))
    conn.commit()
conn.close()



