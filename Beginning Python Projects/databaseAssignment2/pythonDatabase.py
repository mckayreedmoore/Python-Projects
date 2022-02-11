import sqlite3

#tuple containing file names
fileList=('information.docx','hello.txt','myImage.png', \
          'myMovie.mpg','world.txt','data.pdf','myPhoto.jpg')

#declare connection variable
conn = sqlite3.connect('mainDatabase.db')

#while you have a connection, execute this SQL
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data (\
        file_id INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    for file in fileList:
        if file.endswith('txt'):
            cur.execute("INSERT INTO tbl_data (col_file) VALUES (?)",(file,))
            print(file)
    

    
    conn.commit()
conn.close()

