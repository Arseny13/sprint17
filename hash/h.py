def strange_compare(str1, str2):
    mp = {}
    index = 0
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i not in mp.keys():
            if str2[index] in mp.values():
                return False
            mp[i] = str2[index]
        else:
            if mp[i] != str2[index]:
                return False
        index += 1
    return True


def solve_task_h():
    str1 = input()
    str2 = input()
    if strange_compare(str1, str2):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    solve_task_h()
