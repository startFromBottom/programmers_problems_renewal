"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3

"""


def solution(m, n, puddles):
    areas = [[0 for _ in range(m)] for _ in range(n)]
    areas[0][0] = 1

    # 가장자리(가로) setting
    for j in range(m):
        if [j + 1, 1] in puddles:
            break
        areas[0][j] = 1
        # 가장자리(세로) setting
    for i in range(n):
        if [1, i + 1] in puddles:
            break
        areas[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:
                continue
            areas[i][j] = areas[i - 1][j] + areas[i][j - 1]

    return areas[n - 1][m - 1] % 1000000007
