def maxDistance(arr, n):
    mp = {}
    maxDict = 0
    for i in range(n):
        if arr[i] not in mp.keys():
            mp[arr[i]] = i
        else:
            maxDict = max(maxDict, i-mp[arr[i]])
    return maxDict


def solve_task_g():
    n = int(input())
    res = [0]
    arr = [int(x) for x in input().split()]
    sum1 = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
        sum1 += arr[i]
        res.append(sum1)
    print(maxDistance(res, n+1))


if __name__ == '__main__':
    solve_task_g()
