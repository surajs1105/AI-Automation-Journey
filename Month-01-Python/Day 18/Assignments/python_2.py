# Python 2: Insert a new node at the beginning  (O(1))
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

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   # link to old head first
        self.head = new_node        # then move head


ll = LinkedList()
for v in (20, 30, 40):
    ll.insert_end(v)
print("Before:")
ll.display()
ll.insert_beginning(10)
print("After inserting 10 at the beginning:")
ll.display()
