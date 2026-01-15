import sqlite3
import pandas as pd

def analyze_students():
    conn = sqlite3.connect("students.db")

    df = pd.read_sql_query("SELECT * FROM students", conn)

    if df.empty:
        print("\nNo student data available for analysis.")
        conn.close()
        return

    print("\n📊 Student Performance Analysis")

    # Average marks
    avg_marks = df["marks"].mean()
    print(f"\nAverage Marks: {avg_marks:.2f}")

    # Top performing student
    top_student = df.loc[df["marks"].idxmax()]
    print("\n🏆 Top Performing Student:")
    print(f"ID: {top_student['student_id']}")
    print(f"Name: {top_student['name']}")
    print(f"Marks: {top_student['marks']}")

    # Course-wise average marks
    print("\n📚 Course-wise Average Marks:")
    course_avg = df.groupby("course")["marks"].mean()
    print(course_avg)

    conn.close()
