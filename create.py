import sqlite3

#PORT 1

conn = sqlite3.connect('Port1.db')

cursor = conn.cursor()

sql_command1 = '''
    CREATE TABLE IF NOT EXISTS PaltanBazar (
        Id INTEGER PRIMARY KEY,
        Billed_Unit INT, 
        Name TEXT, 
        Rate INT,
        Net_Amount INT,
        Place TEXT DEFAULT 'Paltan Bazar',
        Port INT DEFAULT 1
    )'''
 
sql_command2 = '''
    CREATE TABLE IF NOT EXISTS Panbazar (
        Id INTEGER PRIMARY KEY,
        Billed_Unit INT, 
        Name TEXT, 
        Rate INT,
        Net_Amount INT,
        Place TEXT DEFAULT 'Panbazar',
        Port INT DEFAULT 1
    )'''
 
cursor.execute(sql_command1)
cursor.execute(sql_command2)
 
conn.commit()

conn.close()

#PORT 2

conn = sqlite3.connect('Port2.db')

cursor = conn.cursor()

sql_command1 = '''
    CREATE TABLE IF NOT EXISTS Jalukbari (
        Id INTEGER PRIMARY KEY,
        Billed_Unit INT, 
        Name TEXT, 
        Rate INT,
        Net_Amount INT,
        Place TEXT DEFAULT 'Jalukbari',
        Port INT DEFAULT 2
    )'''
 
sql_command2 = '''
    CREATE TABLE IF NOT EXISTS Adabari (
        Id INTEGER PRIMARY KEY,
        Billed_Unit INT, 
        Name TEXT, 
        Rate INT,
        Net_Amount INT,
        Place TEXT DEFAULT 'Adabari',
        Port INT DEFAULT 2
    )'''
 
cursor.execute(sql_command1)
cursor.execute(sql_command2)
 
conn.commit()

conn.close()




