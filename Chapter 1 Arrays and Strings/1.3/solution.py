from util import TwoWayLinkedList, Node


def URLify(string: str, length: int) -> str:
    """
    Removes all spaces from a string and replaces them with '%20'.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    # convert string to a linked list
    linked_list = TwoWayLinkedList()
    current = linked_list.head
    for char in string:
        if current is None:
            current = Node(char, prev=None)
            linked_list.head = current
        elif char == " ":
            if current.data != "%20":
                current.next = Node("%20", prev=current)
                current = current.next
        else:
            current.next = Node(char, prev=current)
            current = current.next

    # remove trailing space char
    if current.data == "%20":
        current.prev.next = None

    # convert linked list back to string
    current = linked_list.head
    string = ""
    while current is not None:
        string += current.data
        current = current.next

    return string
