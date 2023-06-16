def union(data, n):
    data.sort()
    result = []
    start = data[0][0]
    end = data[0][1]
    for i in range(1, n):
        if end < data[i][0]:
            result.append(f'{start} {end}')
            start = data[i][0]
            end = data[i][1]
        elif end < data[i][1]:
            end = data[i][1]
    result.append(f'{start} {end}')
    return result


def solve_task_n():
    n = int(input())
    data = []
    for _ in range(n):
        data.append(tuple([int(x) for x in input().split(' ')]))
    print('\n'.join(union(data, n)), end='')


if __name__ == '__main__':
    solve_task_n()
