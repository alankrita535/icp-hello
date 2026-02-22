import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{course}\n")

    print("✅ Student added successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No students available.\n")
        return

    print("\n📋 Student List:")
    for line in data:
        name, roll, course = line.strip().split(",")
        print(f"Name: {name} | Roll: {roll} | Course: {course}")
    print()


def search_student():
    roll_search = input("Enter roll number to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, roll, course = line.strip().split(",")
            if roll == roll_search:
                print(f"✅ Found: {name} | {roll} | {course}\n")
                found = True
                break

    if not found:
        print("❌ Student not found.\n")


def delete_student():
    roll_delete = input("Enter roll number to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    lines = []
    deleted = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            name, roll, course = line.strip().split(",")
            if roll != roll_delete:
                file.write(line)
            else:
                deleted = True

    if deleted:
        print("🗑️ Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.\n")


menu()