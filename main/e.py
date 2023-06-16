def solve_task_e():
    n, k = map(int, input().split())
    array = [int(x) for x in input().split()]
    array.sort()
    result = 0
    for i in array:
        if i <= k:
            result += 1
            k -= i
    print(result)


if __name__ == '__main__':
    solve_task_e()
