def hesh_string(string: str, a: int, m: int) -> int:
    result = 0
    for s in string:
        result = (result*a + ord(s)) % m
    return result


def solve_task_a():
    a = 1000 #int(input())
    m = 1000009 #int(input())
    arr = ['a', 'ab', 'abc', 'abcdefgh']
    for i in arr:
        string = 'abcdefgh' #input()
        print(hesh_string(i, a, m))


if __name__ == '__main__':
    solve_task_a()
