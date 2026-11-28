# Day 19 - GATE Practice Questions

1. **Which sorting algorithm performs well on nearly sorted data?**
   **Insertion Sort.** If elements are already close to their final positions, the inner
   `while` loop does very little shifting, so it runs close to O(n). (Optimized bubble sort
   also does well, but insertion sort is the standard answer.)

2. **Worst-case complexity of Quick Sort?**
   **O(n^2)**, when the pivot is always the smallest or largest element (e.g. already
   sorted input with a poor pivot choice). Average case is O(n log n).

3. **Which sorting algorithm has O(n log n) worst-case complexity?**
   **Merge Sort** (also Heap Sort). Merge sort always splits in half and merges in O(n)
   per level.

4. **Time complexity of two nested loops, each running n times?**
   **O(n^2)**: n x n iterations.

5. **How many comparisons does Selection Sort make for n elements?**
   **n(n-1)/2**, which is O(n^2). It always makes the same number of comparisons
   regardless of input order: (n-1) + (n-2) + ... + 1.
