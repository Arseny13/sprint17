# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing
from typing import Tuple

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def tree_sizes(left, right):
    ls, rs = 0, 0
    if left is not None:
        ls = left.size
    if right is not None:
        rs = right.size
    return ls, rs


def split(root, k) -> Tuple[Node, Node]:
    if root is None:
        return None, None
    ls, rs = tree_sizes(root.left, root.right)

    if ls + 1 > k:
        ln, rn = split(root.left, k)
        ln_size, rn_size = tree_sizes(ln, rn)

        root.size = root.size - ls + rn_size

        return ln, root

    ln, rn = split(root.right, k - ls - 1)
    ln_size, rn_size = tree_sizes(ln, rn)
    root.size = root.size - rs + ln_size
    root.right = ln

    return root, rn


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert (left.size == 4)
    assert (right.size == 2)


if __name__ == '__main__':
    test()
