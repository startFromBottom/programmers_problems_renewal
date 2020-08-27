"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

"""

from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))

    def larger_number(n1: str, n2: str) -> int:
        return 1 if n1 + n2 <= n2 + n1 else -1

    res = "".join(sorted(numbers, key=cmp_to_key(larger_number)))
    return "0" if set(res) == {"0"} else res


def solution_timeover(numbers):
    """
    use insertion sort -> time over
    """

    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) <= str(n2) + str(n1)

    for i in range(1, len(numbers)):
        j = i
        while j > 0 and to_swap(numbers[j - 1], numbers[j]):
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
            j -= 1

    return str(int(''.join(map(str, numbers))))
