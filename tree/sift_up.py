def sift_up(heap, idx) -> int:
    while heap[idx] > heap[idx // 2]:
        if idx == 1:
            break
        heap[idx // 2], heap[idx] = heap[idx], heap[idx//2]
        idx = idx // 2
    return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
