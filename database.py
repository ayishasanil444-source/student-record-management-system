import sqlite3

DB_NAME = "students.db"


def connect_db():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        marks REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_student(student):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
        student.to_tuple()
    )

    conn.commit()
    conn.close()


def fetch_all_students():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    conn.close()
    return records


# -------- NEW CRUD OPERATIONS --------

def update_student_marks(student_id, new_marks):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks = ? WHERE student_id = ?",
        (new_marks, student_id)
    )

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()
