# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def find_sum(root):
    if root is None:
        return 0
    left_sum = find_sum(root.left)
    right_sum = find_sum(root.right)

    max_single = max(max(left_sum, right_sum) + root.value, root.value)
    max_top = max(max_single, left_sum + right_sum + root.value)

    find_sum.sum = max(find_sum.sum, max_top)

    return max_single


def solution(root) -> int:
    find_sum.sum = float("-inf")
    find_sum(root)
    return find_sum.sum


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6


if __name__ == '__main__':
    test()
