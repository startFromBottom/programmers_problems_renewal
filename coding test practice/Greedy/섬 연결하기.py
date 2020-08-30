"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3#

"""


def solution(n, costs):
    parents = {}
    for u, v, w in costs:
        parents[u] = u
        parents[v] = v
    set_counts = {k: 1 for k in parents}

    def find(n):
        if parents[n] != n:
            parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        n1 = find(n1)
        n2 = find(n2)
        if n1 != n2:
            if set_counts[n1] >= set_counts[n2]:
                parents[n2] = n1
                set_counts[n1] += set_counts[n2]
            else:
                parents[n1] = n2
                set_counts[n2] += set_counts[n1]

    costs.sort(key=lambda x: x[2])  # sort by cost

    min_cost = 0
    for u, v, c in costs:
        if find(u) == find(v):
            if set_counts[parents[u]] == n:
                break
            continue
        union(u, v)
        min_cost += c

    return min_cost
