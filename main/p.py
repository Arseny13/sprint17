
def solve_task_p():
    n = int(input())
    array = [int(x) for x in input().split()]
    count, first = 0, 0
    for i in range(n):
        aux = array[first:i+1]
        aux.sort()
        isPart = True
        min = first
        for k in aux:
            if k != min:
                isPart = False
                break
            min += 1
        if isPart:
            count += 1
            first = i + 1
    print(count)


if __name__ == '__main__':
    solve_task_p()
