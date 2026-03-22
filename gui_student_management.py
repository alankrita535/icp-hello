import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "students.txt"

# ADD STUDENT
def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    course = entry_course.get()

    if name == "" or roll == "" or course == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{course}\n")

    messagebox.showinfo("Success", "Student added successfully!")

    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_course.delete(0, tk.END)


# VIEW STUDENTS
def view_students():
    text_area.delete("1.0", tk.END)

    if not os.path.exists(FILE_NAME):
        text_area.insert(tk.END, "No records found\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        text_area.insert(tk.END, "No records found\n")
        return

    for line in data:
        text_area.insert(tk.END, line)


# DELETE STUDENT
def delete_student():
    roll = entry_roll.get()

    if roll == "":
        messagebox.showwarning("Warning", "Enter roll number to delete")
        return

    if not os.path.exists(FILE_NAME):
        messagebox.showerror("Error", "No data found")
        return

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        found = False
        for line in lines:
            parts = line.strip().split(",")
            if parts[1] != roll:
                file.write(line)
            else:
                found = True

    if found:
        messagebox.showinfo("Success", "Student deleted successfully!")
    else:
        messagebox.showerror("Error", "Student not found")


# GUI WINDOW
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x450")

# TITLE
tk.Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=10)

# INPUT FIELDS
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll Number").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root)
entry_course.pack()

# BUTTONS
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

# TEXT AREA
text_area = tk.Text(root, height=10)
text_area.pack(pady=10)

# RUN APP
root.mainloop()