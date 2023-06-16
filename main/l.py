def BinarySearch(array, x, left, right):
    if right <= left and left != 0:
        return -1
    middle = (left + right) // 2
    if array[middle] >= x and (array[middle-1] < x or middle == 0):
        return middle + 1
    elif x <= array[middle]:
        return BinarySearch(array, x, left, middle)
    else:
        return BinarySearch(array, x, middle + 1, right)


def solve_task_l():
    count_days = int(input())
    array = [int(x) for x in input().split()]
    price_byke = int(input())
    res1 = BinarySearch(array, price_byke, 0, count_days)
    res2 = BinarySearch(array, 2*price_byke, 0, count_days)
    print(res1, res2)


if __name__ == '__main__':
    solve_task_l()
