# Day 21 - Project review: does the Student Marks Management System actually work?
# Runs the real code from ../03_student_marks_system_week3.py and checks each feature.
# The lesson says: "Do not assume these features are complete - inspect your actual code."
import importlib.util
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "03_student_marks_system_week3.py")
spec = importlib.util.spec_from_file_location("sms", path)
sms = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sms)

results = []


def check(feature, condition):
    results.append((feature, condition))


# Add
check("Add student records", sms.add_student(101, "Amit", 85) is True)
sms.add_student(102, "Rahul", 92)
sms.add_student(103, "Sneha", 78)
sms.add_student(104, "Priya", 88)
check("Rejects duplicate roll number", sms.add_student(101, "X", 50) is False)
check("Rejects invalid marks", sms.add_student(105, "Y", 150) is False)

# Display
check("Display student records (4 stored)", len(sms.students) == 4)

# Search
check("Search by roll number (found)", sms.search_student(102)["name"] == "Rahul")
check("Search by roll number (missing -> None)", sms.search_student(999) is None)

# Average
check("Calculate average marks (85.75)", sms.calculate_average() == 85.75)

# Highest / lowest
top, low = sms.highest_and_lowest()
check("Highest marks (Rahul 92)", top["name"] == "Rahul")
check("Lowest marks (Sneha 78)", low["name"] == "Sneha")

# Sorting / ranking
ranked = [s["name"] for s in sms.sort_by_marks()]
check("Sort by marks descending", ranked == ["Rahul", "Priya", "Amit", "Sneha"])

print("PROJECT REVIEW")
print("=" * 50)
for feature, ok in results:
    print(("[PASS] " if ok else "[FAIL] ") + feature)

print("\nNot yet built (Week 4 plan): grades, file handling (save/load records).")
passed = sum(ok for _, ok in results)
print(f"\n{passed}/{len(results)} checks passed")
