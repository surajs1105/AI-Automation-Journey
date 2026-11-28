# Project 3: display_students() using saved records
def display_students():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No student records found.")
        return

    if not lines:
        print("students.txt is empty.")
        return

    print(f"{'Roll No':<10}{'Name':<12}{'Marks':<6}")
    print("-" * 28)
    for line in lines:
        roll, name, marks = [x.strip() for x in line.strip().split(",")]
        print(f"{roll:<10}{name:<12}{marks:<6}")


display_students()
