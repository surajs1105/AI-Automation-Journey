# Day 21 - Stack (LIFO) and Linked List revision

# ---- Stack using a Python list ----
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())    # 30  (last in, first out)
print(stack)          # [10, 20]


# ---- Singly Linked List ----
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):      # O(1)
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):            # O(n) without a tail pointer
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete_first(self):                # O(1)
        if self.head:
            self.head = self.head.next

    def search(self, target):              # O(n)
        cur = self.head
        while cur:
            if cur.data == target:
                return True
            cur = cur.next
        return False

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


ll = LinkedList()
ll.insert_end(20)
ll.insert_end(30)
ll.insert_beginning(10)
ll.display()                 # 10 -> 20 -> 30 -> None
print("Search 20:", ll.search(20))
print("Search 99:", ll.search(99))
ll.delete_first()
ll.display()                 # 20 -> 30 -> None
