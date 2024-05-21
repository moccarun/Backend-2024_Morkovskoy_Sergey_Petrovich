import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

query = '''
SELECT * FROM Users
WHERE SURNAME LIKE 'А%' AND SALARY >= 100000
'''

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row[1])

conn.close()
