# DSA 3: Insert a new node at the beginning of a Linked List  (O(1))
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
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   # 1. link new node to the old head
        self.head = new_node        # 2. make the new node the head

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
for v in (20, 30, 40):
    ll.insert_end(v)
print("Before:")
ll.display()
ll.insert_beginning(10)
print("After inserting 10 at the beginning:")
ll.display()
