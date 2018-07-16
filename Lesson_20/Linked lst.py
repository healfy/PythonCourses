"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    flag = False
    array = []
    while head.next:
        array.append(head.next)
        head = head.next
        if head.next in array:
            flag = True
            break
    return flag
