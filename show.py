import sqlite3

conn = sqlite3.connect('Port2.db')

cursor = conn.cursor()

select_data = 'SELECT * FROM Jalukbari'
cursor.execute(select_data)
 
row = cursor.fetchall()
 
print(row)
 
# Commit the changes to the database
