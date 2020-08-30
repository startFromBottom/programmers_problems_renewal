"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

"""


def solution(n, lost, reserve):

    reserve = set(reserve)
    temp = lost[:] # deep copy
    for l in temp:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)

    L = len(lost)
    lost.sort()
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
            L -= 1
            continue
        if l + 1 in reserve:
            reserve.remove(l + 1)
            L -= 1

    return n - L
