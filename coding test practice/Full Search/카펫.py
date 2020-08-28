"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

"""

import math


def solution(brown, red):
    total = brown + red
    h = 1
    while h <= math.sqrt(total):
        w = total // h
        if (w - 2) * (h - 2) == red and (w + h) * 2 - 4 == brown:
            return [w, h]
        h += 1
    return None
