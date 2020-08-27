"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

"""

import heapq


def solution(jobs):
    """
    jobs의 각 행 : [작업 요청 시점, 작업의 소요 시간]
    """

    L = len(jobs)
    ans = 0
    time = 0  # 특정 job이 끝났을 때 시간
    min_heap = []
    i = 0
    jobs.sort(key=lambda x: x[0])

    while i < L or min_heap:
        while i < L and jobs[i][0] <= time:
            heapq.heappush(min_heap, list(reversed(jobs[i])))
            i += 1

        if not min_heap:
            time = jobs[i][0]
        else:
            job = list(reversed(heapq.heappop(min_heap)))
            ans += time - job[0] + job[1]
            time += job[1]

    return ans // L
