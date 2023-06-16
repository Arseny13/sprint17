def condition(a, b, c):
    return c < a + b


def solve_task_f():
    n = int(input())
    array = [int(x) for x in input().split()]
    array.sort(reverse=True)
    for i in range(n-2):
        c = array[i]
        b = array[i + 1]
        a = array[i + 2]
        if condition(a, b, c):
            print(a+b+c)
            break


if __name__ == '__main__':
    solve_task_f()
