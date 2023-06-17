# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    curr = root
    prev = None

    while curr is not None:
        if curr.left is None:
            if prev is not None and prev.value >= curr.value:
                return False
            prev = curr
            curr = curr.right
        else:
            pred = curr.left
            while pred.right is not None and pred.right != curr:
                pred = pred.right
            if pred.right is None:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                if prev is not None and prev.value >= curr.value:
                    return False
                prev = curr
                curr = curr.right
    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
