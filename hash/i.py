import collections

a, mod = 101, 1_000_000_000_001


def degree(length):
    result = [1]
    for x in range(length):
        result.append(result[x] * a % mod)
    return result


def create_hash(str, length):
    result = [0] * (length + 1)
    for i in range(length):
        result[i+1] = (result[i]*a + str[i]) % mod
    return result


def get_hash(hash, pow, left, right):
    return (hash[right + 1] - hash[left] * pow[right - left + 1] % mod) % mod


def foundSubArray(pow, hash1, hash2, m, n, nums1, nums2, size):
    seen = collections.defaultdict(list)
    for i in range(n - size + 1):
        h = get_hash(hash1, pow, i, i + size - 1)
        seen[h].append(i)
    for i in range(m - size + 1):
        h = get_hash(hash2, pow, i, i + size - 1)
        if h in seen:
            for j in seen[h]:
                if nums1[j:j + size] == nums2[i:i + size]:
                    return True
    return False


def solve_task_i():
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    m = int(input())
    arr2 = [int(x) for x in input().split()]

    pow = degree(max(m, n))
    hash1 = create_hash(arr1, n)
    hash2 = create_hash(arr2, m)

    left, right, ans = 1, min(m, n), 0
    while left <= right:
        mid = (left + right) // 2
        if foundSubArray(pow, hash1, hash2, m, n, arr1, arr2, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)


if __name__ == '__main__':
    solve_task_i()
