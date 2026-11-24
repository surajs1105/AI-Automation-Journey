# Python 5: Count the total number of nodes
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

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


ll = LinkedList()
print("Empty list count:", ll.count_nodes())
for v in (10, 20, 30, 40, 50):
    ll.insert_end(v)
ll.display()
print("Total nodes:", ll.count_nodes())
