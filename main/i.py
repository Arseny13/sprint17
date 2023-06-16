import collections


def solve_task_i():
    n = int(input())
    c = n
    c = collections.Counter()
    for x in input().split():
        c[int(x)] += 1
    k = int(input())
    result = c.most_common(k)
    for i in result:
        print(i[0], end=' ')


if __name__ == '__main__':
    solve_task_i()
