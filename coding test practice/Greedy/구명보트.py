"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

"""

from collections import deque


def solution(people, limit):
    people.sort()
    q = deque(people)
    cnt = 0

    while q:
        min_v = q.popleft()
        while q and q[-1] + min_v > limit:
            q.pop()
            cnt += 1
        if q:
            q.pop()
        cnt += 1

    return cnt
