def solve_task_g():
    n = int(input())
    count = [0]*3
    for x in input().split():
        if x == '0':
            count[0] += 1
        elif x == '1':
            count[1] += 1
        elif x == '2':
            count[2] += 1
    print(*([0]*count[0] + [1]*count[1] + [2]*count[2]))


if __name__ == '__main__':
    solve_task_g()
