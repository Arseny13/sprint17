COMMAND = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def gen_comb(arr, string):
    if arr == '':
        print(string, end=' ')
        return
    for i in COMMAND[arr[0]]:
        gen_comb(arr[1:], string + i)


def solve_task_b():
    string = input()
    gen_comb(string, '')


if __name__ == '__main__':
    solve_task_b()
