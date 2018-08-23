def insertNodeAtPosition(head, data, position):
    node = SinglyLinkedListNode(data)
    current_node = head

    for _ in range(position - 1):
        current_node = current_node.next

    node.next = current_node.next
    current_node.next = node
    return head


def makeAnagram(a, b):    
    p = Counter(a)
    z = Counter(b)
    d = p - z
    c = z - p
    e = d + c
    return len(list(e.elements()))

def alternatingCharacters(s):
    d = []
    for i in range(len(s) - 1):
        if s[i+1] == s[i]:
            d.append(s[i+1])
    return len(d)
