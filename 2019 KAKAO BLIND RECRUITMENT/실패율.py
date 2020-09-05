"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

"""

from collections import Counter


def solution(N, stages):
    res = []

    c = Counter(stages)
    boonmo = len(stages)

    for i in range(1, N + 1):
        boonza = 0
        for k, v in c.items():
            if k <= i:
                boonza += v
                c[k] = 0
        if boonmo > 0:
            res.append((i, boonza / boonmo))
        else:
            res.append((i, 0))
        boonmo -= boonza

    res.sort(key=lambda k: (-k[1], k[0]))
    return [r[0] for r in res]
