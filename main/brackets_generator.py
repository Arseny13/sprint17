def gen_binary(n, count_open, count_close, prefix):
    if count_close + count_open == 2*n:
        print(prefix)
        return
    if count_open < n:
        gen_binary(n, count_open+1, count_close, prefix + '(')
    if count_open > count_close:
        gen_binary(n, count_open, count_close + 1, prefix + ')')


def solve_task_l():
    count = int(input())
    gen_binary(count, 0, 0, '')


if __name__ == '__main__':
    solve_task_l()
