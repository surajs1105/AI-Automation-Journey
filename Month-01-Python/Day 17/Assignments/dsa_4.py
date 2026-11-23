# DSA 4: Delete the first node and display the updated Linked List  (O(1))
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

    def delete_first(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        self.head = self.head.next   # old head is no longer referenced

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
for v in (10, 20, 30, 40):
    ll.insert_end(v)
print("Before:")
ll.display()
ll.delete_first()
print("After deleting first node:")
ll.display()
