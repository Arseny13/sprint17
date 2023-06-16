def solve_task_d():
    n = int(input())
    child = [int(x) for x in input().split()]
    m = int(input())
    cookie = [int(x) for x in input().split()]
    child.sort(reverse=True)
    cookie.sort()
    result = 0
    for i in range(n):
        if cookie and child[i] <= cookie[-1]:
            cookie.pop()
            result += 1
    print(result)


if __name__ == '__main__':
    solve_task_d()
