"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3

"""


def solution(n, times):
    lo, hi = 0, max(times) * n

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        people = sum([mid // t for t in times])
        if people < n:
            lo = mid + 1
        else:
            hi = mid - 1

    return lo
