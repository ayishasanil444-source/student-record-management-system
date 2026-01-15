from database import (
    create_table,
    insert_student,
    fetch_all_students,
    update_student_marks,
    delete_student
)
from student import Student
from analysis import analyze_students


def menu():
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Analyze Performance")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")


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

    if not students:
        print("⚠️ No student records found.")
        return

    print("\nID | Name | Age | Course | Marks")
    print("-" * 40)

    for s in students:
        print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]}")


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
        new_marks = float(input("Enter new marks: "))

        update_student_marks(student_id, new_marks)
        print("✅ Student marks updated successfully")

    except ValueError:
        print("❌ Invalid input! Enter valid numbers.")


def remove_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        confirm = input("Are you sure you want to delete this student? (y/n): ")

        if confirm.lower() == "y":
            delete_student(student_id)
            print("✅ Student deleted successfully")
        else:
            print("❌ Delete operation cancelled")

    except ValueError:
        print("❌ Invalid input! Enter a valid student ID.")


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
            update_student()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            print("👋 Exiting Program...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
