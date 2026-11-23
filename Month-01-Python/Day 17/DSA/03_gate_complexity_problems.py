# Day 17 - GATE problems (complexity)
n = 100

# Problem 1: i doubles each time -> O(log n)
i = 1
count = 0
while i < n:
    i = i * 2
    count += 1
print("Problem 1 iterations:", count, "(~log2 n)")

# Problem 2: outer n x inner 5 = 5n -> O(n)
count = 0
for i in range(n):
    for j in range(5):
        count += 1
print("Problem 2 operations:", count, "= 5n")

# Problem 3: traversal of n nodes -> O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
for v in range(n, 0, -1):          # build list of n nodes
    node = Node(v)
    node.next = head
    head = node

visited = 0
current = head
while current is not None:
    visited += 1
    current = current.next
print("Problem 3 nodes visited:", visited)
