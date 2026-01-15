from database import create_table, insert_student, fetch_all_students
from student import Student
from analysis import analyze_students


def menu():
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Analyze Performance")
    print("4. Exit")


def add_student():
    try:
        student_id = int(input("Enter ID (unique number): "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        student = Student(student_id, name, age, course, marks)
        insert_student(student)

        print("✅ Student added successfully")

    except ValueError:
        print("❌ Invalid input! Please enter numbers for ID, age, and marks.")
    except Exception as e:
        if "UNIQUE constraint failed" in str(e):
            print("❌ Student ID already exists. Use a different ID.")
        else:
            print("❌ Error:", e)


def view_students():
    students = fetch_all_students()

    print("\nID | Name | Age | Course | Marks")
    print("-" * 40)

    for s in students:
        print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]}")


def main():
    create_table()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            analyze_students()
        elif choice == "4":
            print("👋 Exiting Program...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
