def merge(arr, lf, mid, rg):
    left, right = lf, mid
    result = []
    while left < mid and right < rg:
        if arr[left] <= arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right += 1
    if left < mid:
        result += arr[left:mid]
    if right < rg:
        result += arr[right:rg]
    return result


def merge_sort(arr, lf, rg):
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
