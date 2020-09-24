"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3

"""

from collections import defaultdict, deque


def solution(n, edge):
    ans = 0
    graph = defaultdict(list)
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)

    visited = {1}
    q = deque([1])

    while q:
        l = len(q)
        ans = l
        for _ in range(l):
            node = q.popleft()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    q.append(next_node)
    return ans
