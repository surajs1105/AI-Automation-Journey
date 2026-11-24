# Python 3: Search for a value in a linked list  (O(n))
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, target):
        current = self.head
        position = 0
        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1


ll = LinkedList()
for v in (10, 20, 30, 40, 50):
    ll.insert_end(v)
ll.display()

for target in (30, 99):
    pos = ll.search(target)
    if pos != -1:
        print(f"{target} found at position {pos} (0-based)")
    else:
        print(f"{target} not found")
