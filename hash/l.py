a, mod = 31, 2305843009213693951  # надо выбирать норм константы


def degree(length):
    result = [1]
    for x in range(length):
        result.append(result[x] * a % mod)
    return result


def create_hash(str, length):
    result = [0] * (length + 1)
    for i in range(length):
        result[i+1] = ((result[i]*a) % mod + ord(str[i])) % mod
    return result


def get_hash(hash, pow, left, right):
    return (hash[right + 1] - (hash[left] * pow[right - left + 1]) % mod) % mod


def solve_task_l():
    n, k = map(int, input().split())
    s = input()
    d = {}
    pow = degree(len(s))
    hash = create_hash(s, len(s))
    for i in range(len(s) - n):
        x = get_hash(hash, pow, i, i + n - 1)
        if x not in d.keys():
            d[x] = [i, 1]
        else:
            d[x][1] += 1
            if d[x][1] == k:
                print(d[x][0], end=' ')


if __name__ == '__main__':
    solve_task_l()
