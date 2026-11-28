# DSA 3: Time complexity of Bubble, Selection and Insertion Sort
#
# | Algorithm       | Best   | Average | Worst  |
# |-----------------|--------|---------|--------|
# | Bubble Sort*    | O(n)   | O(n^2)  | O(n^2) |
# | Selection Sort  | O(n^2) | O(n^2)  | O(n^2) |
# | Insertion Sort  | O(n)   | O(n^2)  | O(n^2) |
# *Optimized bubble sort with early exit.
#
# Space complexity: all three are in-place -> O(1).

rows = [
    ("Bubble Sort*",   "O(n)",   "O(n^2)", "O(n^2)"),
    ("Selection Sort", "O(n^2)", "O(n^2)", "O(n^2)"),
    ("Insertion Sort", "O(n)",   "O(n^2)", "O(n^2)"),
]
print(f"{'Algorithm':<16}{'Best':<10}{'Average':<10}{'Worst':<10}")
for r in rows:
    print(f"{r[0]:<16}{r[1]:<10}{r[2]:<10}{r[3]:<10}")
print("*Optimized bubble sort")
