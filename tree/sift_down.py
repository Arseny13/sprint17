def sift_down(heap, idx) -> int:
    while 2*idx < len(heap):
        left = idx*2
        right = idx*2 + 1
        if right < len(heap) and heap[left] < heap[right]:
            max = right
        else:
            max = left
        if heap[max] > heap[idx]:
            heap[idx], heap[max] = heap[max], heap[idx]
            idx = max
        else:
            break
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
