# Day 19 - GATE: sorting algorithm complexity table
rows = [
    ("Bubble Sort*",   "O(n)",       "O(n^2)",     "O(n^2)"),
    ("Selection Sort", "O(n^2)",     "O(n^2)",     "O(n^2)"),
    ("Insertion Sort", "O(n)",       "O(n^2)",     "O(n^2)"),
    ("Merge Sort",     "O(n log n)", "O(n log n)", "O(n log n)"),
    ("Quick Sort",     "O(n log n)", "O(n log n)", "O(n^2)"),
]

print(f"{'Algorithm':<16}{'Best':<13}{'Average':<13}{'Worst':<13}")
print("-" * 55)
for name, best, avg, worst in rows:
    print(f"{name:<16}{best:<13}{avg:<13}{worst:<13}")
print("*Optimized bubble sort (early exit)")
