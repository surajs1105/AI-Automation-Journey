# Day 17 - GATE CS Assignments

## 1. Time complexity of accessing the 5th node in a singly linked list
A linked list has no index. Starting from `head`, we must follow `next` 4 times to reach
the 5th node. In general, reaching the k-th node takes k-1 hops, so **access by index is
O(n)** in the worst case (only the first node is O(1)). For the fixed position 5 it is
exactly 4 hops, but the standard complexity answer is **O(n)**.

## 2. Time complexity of inserting at the beginning of a singly linked list
**O(1).** Only two pointer updates are needed, regardless of list size:
```
new_node.next = head
head = new_node
```
No traversal is required.

## 3. Linked list of 100 nodes - nodes visited in a complete traversal
**100 nodes.** Traversal starts at the head and moves with `current = current.next` until
`current` becomes `None`, visiting each node exactly once. For n nodes the cost is
**O(n)**, so here 100 visits.
