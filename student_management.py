import json
import os

FILE_NAME = "students.json"
print("File path:", os.path.abspath(FILE_NAME))

# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save students to file``
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = {
            "Name": name,
            "Roll": roll,
            "Marks": marks
        }

        students.append(student)
        save_students(students)

        print(" Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for student in students:
                print(
                    f"Name: {student['Name']}, "
                    f"Roll: {student['Roll']}, "
                    f"Marks: {student['Marks']}"
                )

    elif choice == "3":
        roll = input("Enter roll number to search: ")

        found = False
        for student in students:
            if student["Roll"] == roll:
                print("\nStudent Found:")
                print(student)
                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number to update: ")

        found = False
        for student in students:
            if student["Roll"] == roll:
                student["Name"] = input("Enter new name: ")
                student["Marks"] = input("Enter new marks: ")

                save_students(students)

                print(" Student updated successfully!")
                found = True
                break

        if not found:
            print(" Student not found.")

    elif choice == "5":
        roll = input("Enter roll number to delete: ")

        found = False
        for student in students:
            if student["Roll"] == roll:
                students.remove(student)

                save_students(students)

                print(" Student deleted successfully!")
                found = True
                break

        if not found:
            print(" Student not found.")

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print(" Invalid choice. Try again.")