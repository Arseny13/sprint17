
def solve_task_f():
    count_request = int(input())
    arr = [x for x in input().split()]
    d = {}
    for i in range(count_request):
        elem = ''.join(sorted(arr[i]))
        if elem not in d:
            d[elem] = [i]
        else:
            d[elem].append(i)
    for x in d.values():
        print(*x)


if __name__ == '__main__':
    solve_task_f()
