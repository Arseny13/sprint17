# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key) -> Node:
    curr = root
    while True:
        if key < curr.value:
            if curr.left is None:
                curr.left = Node(value=key)
                break
            curr = curr.left
        if key >= curr.value:
            if curr.right is None:
                curr.right = Node(value=key)
                break
            curr = curr.right
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
