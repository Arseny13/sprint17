def degree(a, m, length):
    result = [1]
    for x in range(length):
        result.append(result[x] * a % m)
    return result


def hash_string(string: str, a: int, m: int) -> int:
    result = [0]
    x = 0
    for s in string:
        x = (x*a + ord(s)) % m
        result.append(x)
    return result


def solve_task_c():
    a = int(input())
    m = int(input())
    string = input()
    arr = hash_string(string, a, m)
    power = degree(a, m, len(string)-1)
    count_request = int(input())
    for _ in range(count_request):
        left, right = input().split()
        left, right = int(left), int(right)
        if left == 1:
            print(arr[right])
        elif left == right:
            print(ord(string[right-1]))
        else:
            pow = power[right - left + 1]
            print((arr[right] - arr[left-1]*pow) % m)


if __name__ == '__main__':
    solve_task_c()
