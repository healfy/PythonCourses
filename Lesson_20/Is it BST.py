class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n4.left = n2
n4.right = n6
n2.left = n1
n2.right = n3
n6.left = n5
n6.right = n7


def check_bst(root):
    array = []
    check_root(root, array)
    if array == sorted(array) and array == list(set(array)):
        return True
    else:
        return False


def check_root(root, array):
    if root.left:
        check_root(root.left, array)
    array.append(root.data)
    if root.right:
        check_root(root.right, array)
    return array


print(check_bst(n4))
