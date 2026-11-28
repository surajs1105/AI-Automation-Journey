# Day 21 - Student Marks Management System: Week 3 version
# Combines Day 19 (add/display) and Day 20 (search/average/ranking),
# plus highest/lowest and sorting from the planned feature list.
# Still to come in Week 4: grades and file handling (save/load).

students = []


def add_student(roll_no, name, marks):
    for s in students:
        if s["roll_no"] == roll_no:
            print(f"Roll number {roll_no} already exists - not added")
            return False
    if not (0 <= marks <= 100):
        print("Marks must be between 0 and 100 - not added")
        return False
    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    return True


def display_students():
    if not students:
        print("No students to display")
        return
    print(f"{'Roll No':<10}{'Name':<12}{'Marks':<6}")
    print("-" * 28)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<12}{s['marks']:<6}")


def search_student(roll_no):
    for s in students:
        if s["roll_no"] == roll_no:
            return s
    return None


def calculate_average():
    if not students:
        return None
    return sum(s["marks"] for s in students) / len(students)


def highest_and_lowest():
    if not students:
        return None, None
    top = max(students, key=lambda s: s["marks"])
    low = min(students, key=lambda s: s["marks"])
    return top, low


def sort_by_marks(descending=True):
    return sorted(students, key=lambda s: s["marks"], reverse=descending)


def display_ranking():
    for rank, s in enumerate(sort_by_marks(), start=1):
        print(rank, s["name"], s["marks"])


if __name__ == "__main__":
    add_student(101, "Amit", 85)
    add_student(102, "Rahul", 92)
    add_student(103, "Sneha", 78)
    add_student(104, "Priya", 88)

    print("--- All students ---")
    display_students()

    print("\n--- Search roll 102 ---")
    print(search_student(102) or "Student Not Found")

    print("\n--- Average ---")
    print("Average Marks:", calculate_average())

    print("\n--- Highest / Lowest ---")
    top, low = highest_and_lowest()
    print("Highest:", top["name"], top["marks"])
    print("Lowest :", low["name"], low["marks"])

    print("\n--- Ranking ---")
    display_ranking()
