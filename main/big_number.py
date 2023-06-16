def sort_buble(array, n):
    for i in range(n-1):
        for j in range(n-1-i):
            var1 = array[j] + array[j+1]
            var2 = array[j+1] + array[j]
            if var1 < var2:
                array[j], array[j+1] = array[j+1], array[j]
    print(*array, sep='')


def solve_task_h():
    n = int(input())
    array = [x for x in input().split()]
    sort_buble(array, n)


if __name__ == '__main__':
    solve_task_h()
