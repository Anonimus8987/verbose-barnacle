import sqlite3


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
''')


students_data = [
    ('John Doe', 20, 'A'),
    ('Jane Smith', 22, 'B'),
    ('Bob Johnson', 21, 'C'),
    ('Alice Brown', 19, 'A'),
]

cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students_data)
conn.commit()


def get_student_by_name(student_name):
    cursor.execute('SELECT name, age, grade FROM students WHERE name = ?', (student_name,))
    return cursor.fetchone()


def update_student_grade(student_name, new_grade):
    cursor.execute('UPDATE students SET grade = ? WHERE name = ?', (new_grade, student_name))
    conn.commit()


def delete_student(student_name):
    cursor.execute('DELETE FROM students WHERE name = ?', (student_name,))
    conn.commit()


print("Информация о студенте John Doe до обновления:")
print(get_student_by_name('John Doe'))

update_student_grade('John Doe', 'B')

print("Информация о студенте John Doe после обновления:")
print(get_student_by_name('John Doe'))

delete_student('Jane Smith')


conn.close()
