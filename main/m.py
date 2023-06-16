def solve_task_m():
    n = int(input())
    m = int(input())
    array_n = [int(x) for x in input().split()]
    array_m = [int(x) for x in input().split()]
    index_1 = 0
    index_2 = 0
    x, y = 0, 0
    for i in range((n+m)//2 + 1):
        y = x
        if index_1 >= n:
            x = array_m[index_2]
            index_2 += 1
            continue
        if index_2 >= m:
            x = array_n[index_1]
            index_1 += 1
            continue
        if array_n[index_1] < array_m[index_2]:
            x = array_n[index_1]
            index_1 += 1
        else:
            x = array_m[index_2]
            index_2 += 1
    if (n + m) % 2 != 0:
        print(x)
    else:
        res = (x + y)/2
        if res % 1 == 0:
            print(int(res))
        else:
            print(res)


if __name__ == '__main__':
    solve_task_m()
