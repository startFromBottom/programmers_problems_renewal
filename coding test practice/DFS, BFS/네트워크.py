"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

"""


class Node:
    def __init__(self, idx, visited):
        self.idx = idx
        self.visited = visited


def adjacency_matrix_to_list(n, computers):
    adjs = {}
    for i in range(n):
        linked = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                linked.append(j)
        adjs[i] = linked

    return adjs


def dfs(node, nodes, adjs):
    stack = []
    if node.visited:
        return 0
    stack.append(node.idx)
    nodes[node.idx].visited = True
    while stack:
        pop = stack.pop()
        pop_adjs = adjs[pop]
        if not pop_adjs:
            break
        for i in pop_adjs:
            if not nodes[i].visited:
                stack.append(i)
                nodes[i].visited = True
    return 1


def solution(n, computers):
    answer = 0
    adjs = adjacency_matrix_to_list(n, computers)
    nodes = [Node(idx=i, visited=False) for i in range(n)]
    for node in nodes:
        answer += dfs(node, nodes, adjs)
    return answer
