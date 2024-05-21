import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Department (
    DEPARTMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DEPARTMENT_NAME TEXT NOT NULL
)
''')

departments = [
    ('Backend',),
    ('DevOps',),
    ('Android',),
    ('iOS',)
]
cursor.executemany('''
INSERT INTO Department (DEPARTMENT_NAME) VALUES (?)
''', departments)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    SURNAME TEXT NOT NULL,
    DEPARTMENT_ID INTEGER,
    SALARY INTEGER,
    FOREIGN KEY (DEPARTMENT_ID) REFERENCES Department(DEPARTMENT_ID)
)
''')

users = [
    ('Алексеев', 3, 50000),
    ('Петрухин', 3, 60000),
    ('Есенин', 2, 70000),
    ('Маяковский', 1, 80000),
    ('Нортон', 4, 90000),
    ('Антропов', 1, 100000),
    ('Андреев', 4, 110000),
    ('Силантьев', 1, 120000)
]
cursor.executemany('''
INSERT INTO Users (SURNAME, DEPARTMENT_ID, SALARY) VALUES (?, ?, ?)
''', users)

conn.commit()
conn.close()
