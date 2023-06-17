# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def get_path(root, curr):
    if root is None:
        return 0
    curr = curr * 10 + root.value
    if root.left is None and root.right is None:
        return curr
    return get_path(root.left, curr) + get_path(root.right, curr)


def solution(root) -> int:
    return get_path(root, 0)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()
