
def solve_task_d():
    n = int(input())
    dict = {}
    for i in range(n):
        str = input()
        if str not in dict.keys():
            dict[str] = 0
            print(str)


if __name__ == '__main__':
    solve_task_d()
