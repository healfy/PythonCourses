def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    current_node = head

    for _ in range(position - 1):
        current_node = current_node.next

    node.next = current_node.next
    current_node.next = node
    return head
