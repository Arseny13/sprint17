def solve(arr, k):
    arr.sort()
    length = len(arr)
    le, ri = 0, arr[-1] - arr[0]
    while le < ri:
        mid = (le + ri) // 2
        tmp = 0
        lp = 0
        for i in range(1, length):
            while arr[i] - arr[lp] > mid:
                lp += 1
            tmp += (i-lp)
        if tmp >= k:
            ri = mid
        else:
            le = mid + 1
    return le


def solve_task_o():
    n = int(input())
    array = [int(x) for x in input().split()]
    k = int(input())
    print(solve(array, k))


if __name__ == '__main__':
    solve_task_o()
