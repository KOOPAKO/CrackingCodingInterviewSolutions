from __future__ import annotations  # allow self-reference in class definition


class Node:
    def __init__(self, data: int, next: Node = None, prev: Node = None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        if self.next is None:
            return str(self.data)
        else:
            return str(self.data) + " -> " + str(self.next)


class TwoWayLinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def __str__(self):
        if self.head is None:
            return "[]"
        else:
            return "[" + str(self.head) + "]"
