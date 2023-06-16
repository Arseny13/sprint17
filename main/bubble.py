def sort_buble(array, n):
    k = 0
    for i in range(n-1):
        flag = 0
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 1
                k += 1
        if flag == 0:
            return k
        print(*array)


def solve_task_j():
    n = int(input())
    array = [int(x) for x in input().split()]
    if sort_buble(array, n) == 0:
        print(*array)


if __name__ == '__main__':
    solve_task_j()
