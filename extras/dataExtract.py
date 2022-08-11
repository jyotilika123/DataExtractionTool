import sqlite3
import pandas as pd
conn = sqlite3.connect('Port1.db')

cursor = conn.cursor()

df = pd.read_sql('select * from PaltanBazar', conn)
df.to_csv('apdcl.csv', mode='a', index=False, header=False)
print(df)
conn.close()
# Commit the changes to the database
