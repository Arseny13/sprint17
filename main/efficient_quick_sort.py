# id = 87595660
import random


class User:
    """Класс участников соревнования."""

    def __init__(self, name, tasks, errors) -> None:
        self.__name: str = name
        self.__tasks: int = tasks
        self.__errors: int = errors

    def __gt__(self, other):
        """Метод сравнения "больше чем"."""
        return (
            (self.__tasks, other.__errors, other.__name)
            < (other.__tasks, self.__errors, self.__name)
        )

    def __str__(self) -> str:
        """Метод печати."""
        return self.__name


def quick_sort(array, lt, rt):
    """Быстрая сортировка. Аргументы - массив, начало и конец."""
    if lt >= rt:
        return -1

    pivot = array[random.randint(lt, rt)]
    left, right = lt, rt
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quick_sort(array, lt, right)
    quick_sort(array, left, rt)


def solve_task_b():
    count_users = int(input())
    users = []
    for _ in range(count_users):
        name, tasks, errors = input().split()
        users.append(User(name, int(tasks), int(errors)))
    quick_sort(users, 0, count_users - 1)
    print(*users, sep='\n')


if __name__ == '__main__':
    solve_task_b()
