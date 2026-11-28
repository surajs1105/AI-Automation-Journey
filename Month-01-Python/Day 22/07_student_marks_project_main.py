# Day 22 - Project: Student Marks Management System with permanent storage
# Save as main.py inside StudentMarksManagement/ (students.txt is created automatically).

FILENAME = "students.txt"


def add_student(roll=None, name=None, marks=None):
    # Ask for input only when values are not passed in
    if roll is None:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

    with open(FILENAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")
    print("Record Saved Successfully!")


def display_students():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\n1. Add student\n2. Display students\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
