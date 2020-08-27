"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42747

"""


def solution(citations):
    n = len(citations)
    h = 0
    while h <= n:
        num_uppers = len([c for c in citations if c >= h])
        if h > num_uppers:
            return h - 1
        h += 1
    return n
