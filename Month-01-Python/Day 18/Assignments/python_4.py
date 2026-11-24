# Python 4: Delete a node containing a given value
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

    def delete_value(self, target):
        if self.head is None:
            print("List is empty")
            return False

        # Case 1: the head holds the value
        if self.head.data == target:
            self.head = self.head.next
            return True

        # Case 2: value is further down - keep track of the previous node
        previous = self.head
        current = self.head.next
        while current:
            if current.data == target:
                previous.next = current.next   # skip the node
                return True
            previous = current
            current = current.next

        print(f"{target} not found")
        return False


ll = LinkedList()
for v in (10, 20, 30, 40, 50):
    ll.insert_end(v)
print("Original:")
ll.display()

ll.delete_value(30)
print("After deleting 30:")
ll.display()

ll.delete_value(10)
print("After deleting 10 (head):")
ll.display()

ll.delete_value(99)
