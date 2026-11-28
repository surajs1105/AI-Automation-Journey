# Day 20 - GATE CS Practice

## Solve all five complexity problems

**Q1. Worst-case complexity of Binary Search?**
**O(log n).** Each step halves the search space.

**Q2. Which of Merge Sort and Quick Sort guarantees O(n log n) worst-case time?**
**Merge Sort.** Quick Sort's worst case is O(n^2) (bad pivots), though its average is O(n log n).

**Q3. `i = 1; while i < n: i = i * 3`**
i takes values 1, 3, 9, 27, ... 3^k. It stops when 3^k >= n, i.e. after about log3(n)
iterations. Since log3(n) = log2(n) / log2(3), it differs from log2(n) only by a constant
factor. **O(log n).**

**Q4. `for i in range(n): for j in range(i): ...`**
Inner loop runs 0, 1, 2, ..., n-1 times, so the total is
0 + 1 + ... + (n-1) = n(n-1)/2, which is **O(n^2)**.

**Q5. Total comparisons by Selection Sort for n elements?**
(n-1) + (n-2) + ... + 1 = **n(n-1)/2**, which is O(n^2), regardless of input order.

## Why is Binary Search O(log n)?
Each comparison discards half the remaining elements: n -> n/2 -> n/4 -> ... -> 1.
The number of halvings needed to reach size 1 is k where n / 2^k = 1, so k = log2(n).
Each step does constant work (one comparison), so total work is O(log n). Example: for
n = 1,000,000 elements, at most about 20 comparisons are needed.

## Divide and Conquer using Merge Sort
Divide and Conquer solves a problem in three phases:
1. **Divide** - break the problem into smaller subproblems of the same kind.
   Merge Sort splits the list into two halves.
2. **Conquer** - solve the subproblems recursively. A list of 0 or 1 elements is the
   base case (already sorted).
3. **Combine** - merge the solutions. Merge Sort merges two sorted halves in O(n) by
   repeatedly taking the smaller front element.

Example: [8, 4, 2, 6] -> [8,4] [2,6] -> [8] [4] [2] [6] -> [4,8] [2,6] -> [2,4,6,8].
Recurrence: T(n) = 2T(n/2) + O(n), which solves to **O(n log n)** (log n levels, O(n) work
per level).
