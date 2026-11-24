# Day 18 - GATE CS Practice

## 1. Time complexity of two nested loops
```python
for i in range(n):
    for j in range(n):
        ...
```
The outer loop runs n times and, for each pass, the inner loop runs n times, so the body
runs n x n = n^2 times. **Time complexity: O(n^2).**

(If the inner loop ran a fixed number of times, e.g. 5, the total would be 5n = O(n).
It is O(n^2) when both loops depend on n.)

## 2. Time complexity of a loop that doubles its variable
```python
i = 1
while i < n:
    i = i * 2
```
Values of i: 1, 2, 4, 8, ... 2^k. The loop stops when 2^k >= n, i.e. after about
k = log2(n) iterations. **Time complexity: O(log n).**

## 3. Why does binary search require sorted data?
Binary search compares the target with the middle element and then discards one half
entirely. That decision is only valid if the order tells us which half the target can be
in:
- if target > middle, then (in sorted data) everything on the left is smaller, so the
  target can only be on the right;
- if target < middle, the target can only be on the left.

In unsorted data, the middle comparison says nothing about the positions of other
elements, so discarding a half could throw away the target. Without sorted order,
the algorithm would be incorrect and you would have to fall back to linear search, O(n).
Binary search gets O(log n) only because sorted order lets it halve the search space
each step. (Sorting first costs O(n log n), so it pays off when you search many times.)
