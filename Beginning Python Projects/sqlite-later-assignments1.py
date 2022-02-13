import sqlite3

#get personal data from use
firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
age = int(input("Enter your age: "))

#execute insert statement for supplied person data
with sqlite3.connect('db_test.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+firstName+"','"+ lastName +"'," + str(age) +")"
    c.execute(line)

    
