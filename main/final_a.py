# id = 87595726
def broken_search(nums, target) -> int:
    """Бинарный поиск для "сломанного" массива."""
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (right + left) // 2
        nums_middle = nums[middle]
        if nums_middle == target:
            return middle
        nums_left = nums[left]
        nums_right = nums[right]
        if nums_left <= nums_middle:
            if nums_left <= target < nums_middle:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if nums_middle < target <= nums_right:
                left = middle + 1
            else:
                right = middle - 1
    return -1


def solve_task_a():
    count_element = int(input())
    find_element = int(input())
    array = [int(x) for x in input().split()]
    print(broken_search(array, find_element))


if __name__ == '__main__':
    solve_task_a()
