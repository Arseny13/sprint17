from collections import defaultdict


def find_sum(arr, n, sum):
    d = defaultdict(list)
    for i in range(n-1):
        for j in range(i+1, n):
            s = arr[i] + arr[j]
            d[s].append([i, j])
    res = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if (sum - s) in d:
                p = d[sum-s]
                for k in p:
                    if (k[0] != i and k[0] != j and k[1] != i and k[1] != j):
                        x = [arr[i], arr[j], arr[k[0]], arr[k[1]]]
                        x.sort()
                        if x not in res:
                            res.append(x)
    res.sort()
    print(len(res))
    for i in res:
        print(*i)


def solve_task_j():
    n = int(input())
    s = int(input())
    arr = [int(x) for x in input().split()]
    find_sum(arr, n, s)


if __name__ == '__main__':
    solve_task_j()
