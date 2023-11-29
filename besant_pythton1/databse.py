import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='Srikanth@123',
    port='3306',
    database='animals'
)
mycursor = mydb.cursor()
mycursor.execute('select * from dogs')
dogs = mycursor.fetchall()
for user in dogs:
    print(user)

## If you want to close the database connection
mydb.close()


