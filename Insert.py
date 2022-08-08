import sqlite3

conn = sqlite3.connect('Port2.db')

cursor = conn.cursor()

sql = """
    INSERT INTO Jalukbari 
    (Id, Billed_Unit, Name, Rate, Net_Amount) 
    VALUES (?, ?, ?, ?, ?)
"""

# Id = input("Enter Id: ")
Id = input("Enter Unique Id: ")
BilledUnit = input("Enter BilledUnit: ")
Name = input("Enter Name: ")
Rate = input("Enter Rate: ")
NetAmount = input("Enter NetAmount: ")

conn.execute(sql, (Id, BilledUnit, Name, Rate, NetAmount ))

# Commit the changes to the database
conn.commit()