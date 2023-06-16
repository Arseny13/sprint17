
def solve_task_d():
    str = input()
    res = 0
    cnt = 0
    sub = ''
    for char in str:
        if char not in sub:
            sub += char
            cnt += 1
        else:
            cut = sub.index(char)
            sub = sub[cut+1:] + char
            cnt = len(sub)

        if cnt > res:
            res = cnt

    print(res)


if __name__ == '__main__':
    solve_task_d()
