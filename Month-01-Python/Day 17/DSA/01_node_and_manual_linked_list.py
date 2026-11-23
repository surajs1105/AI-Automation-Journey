# Day 17 - DSA: Node, manual linked list, traversal, insert, delete

# 6.2 Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
print(node1.data)
print(node1.next)

# 6.3 Creating a linked list: 10 -> 20 -> 30 -> None
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
head = node1

# 6.4 Traversal
current = head
while current is not None:
    print(current.data)
    current = current.next

# 6.5 Insert 15 after 10 (connect new node forward FIRST, then update previous)
new_node = Node(15)
new_node.next = node1.next
node1.next = new_node

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# 6.6 Delete node 15
node1.next = new_node.next

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
