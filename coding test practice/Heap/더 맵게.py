"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3

"""

import heapq


def solution(scoville, K):
    mix_cnt = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2:
        f1 = heapq.heappop(scoville)
        if f1 >= K:
            break
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1 + f2 * 2)
        mix_cnt += 1
    if scoville[0] < K:
        return -1
    return mix_cnt
