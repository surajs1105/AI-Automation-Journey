# DSA 1: Node class and a Linked List containing five nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = [10, 20, 30, 40, 50]
nodes = [Node(v) for v in values]

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

head = nodes[0]

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
