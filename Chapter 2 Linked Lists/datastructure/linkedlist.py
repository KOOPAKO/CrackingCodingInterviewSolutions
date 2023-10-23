class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_list(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

    def delete(self, data):
        current = self.head
        previous = None
        while (current and current.data != data):
            previous = current
            current = current.next
        if (current):
            if (previous):
                previous.next = current.next
            else:
                self.head = current.next
            current.next = None
        else:
            print("Data not found")

