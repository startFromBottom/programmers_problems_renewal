"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

"""

from collections import deque


def solution(priorities, location):
    order = 0

    sorted_priorities = sorted(priorities)
    q = deque([(i, p) for i, p in enumerate(priorities)])

    while q:
        i, p = q.popleft()
        if p == sorted_priorities[-1]:
            order += 1
            sorted_priorities.pop()
            if i == location:
                break
        else:
            q.append((i, p))

    return order
