# Day 21 - GATE Examples Explained

## Example 1
```python
for i in range(n):
    print(i)
```
One loop, n iterations, constant work each. **O(n).**

## Example 2
```python
i = 1
while i < n:
    i *= 2
```
i = 1, 2, 4, 8, ... 2^k. Stops when 2^k >= n, i.e. after log2(n) iterations. **O(log n).**

## Example 3
```python
for i in range(n):
    for j in range(i):
        print(i, j)
```
Inner loop runs 0, 1, 2, ..., n-1 times. Total = n(n-1)/2 = (n^2 - n)/2. Drop the
constant and the lower-order term: **O(n^2).** This is not "n x n", but it is still
quadratic.

## Example 4
```python
for i in range(n):
    for j in range(5):
        print(i, j)
```
Total = n x 5 = 5n. The inner loop is a fixed 5 and does not depend on n, so constants
are dropped: **O(n).**

## Key takeaway (your weak area: Time Complexity)
Do not memorise "nested loops = O(n^2)". Ask for each loop: how many times does it run,
and does that depend on n? Then multiply for nested loops and add for consecutive loops.
