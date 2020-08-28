"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

"""

import math
from typing import List
from itertools import permutations


def is_prime_number(n: int) -> bool:
    if n == 1 or n % 2 == 0:
        return False
    k = math.sqrt(n)
    i = 3
    while i <= k:
        if n % i == 0:
            return False
        i += 2
    return True


def all_permutations(numbers: str) -> List[int]:
    N = len(numbers)
    res = []
    for i in range(1, N + 1):
        case = list((map(lambda x: int("".join(x)), list(permutations(numbers, i)))))
        res.extend(case)
    return list(set(res))


def solution(numbers):
    all_cases = all_permutations(numbers)
    return len([n for n in all_cases if is_prime_number(n)])
