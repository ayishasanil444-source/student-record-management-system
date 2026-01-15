from database import create_table, insert_student, fetch_all_students
from student import Student

def menu():
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

def add_student():
    student_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    student = Student(student_id, name, age, course, marks)
    insert_student(student)

    print("✅ Student added successfully")

def view_students():
    students = fetch_all_students()
    print("\nID | Name | Age | Course | Marks")
    print("-" * 35)
    for s in students:
        print(f"{s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]}")

def main():
    create_table()

    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
