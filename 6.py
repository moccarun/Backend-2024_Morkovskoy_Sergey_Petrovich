import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

query = '''
SELECT 
    d.DEPARTMENT_NAME,
    COUNT(u.USER_ID) AS EmployeeCount,
    AVG(u.SALARY) AS AverageSalary
FROM 
    Department d
LEFT JOIN 
    Users u ON d.DEPARTMENT_ID = u.DEPARTMENT_ID
GROUP BY 
    d.DEPARTMENT_NAME
'''

cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(f"Отдел: {row[0]}, Количество сотрудников: {row[1]}, Средняя зарплата: {row[2]}")

conn.close()
