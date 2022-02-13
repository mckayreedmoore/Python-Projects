import sqlite3

#get personal data from user and insert into a tuple
firstName = input("Enter your first nname: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

#execute insert statement for supplied person data
with sqlite3.connect('db_test.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO Peope VALUES(?, ?, ?)", personData)

    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",(45,'Luigi','Vercotti'))
    
    
