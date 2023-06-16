def check_subsequence(string_1, string_2):
    position = -1
    for i in string_1:
        position = string_2.find(i, position + 1)
        if position == -1:
            return False
    return True


def solve_task_c():
    s = input()
    t = input()
    print(check_subsequence(s, t))


if __name__ == '__main__':
    solve_task_c()
