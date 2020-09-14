"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3

"""


def solution(triangle):
    # move to left or right
    N = len(triangle)
    first = triangle[0][0]
    values = [first]
    memo = [[0 for _ in range(len(triangle[i]))] for i in range(N)]
    memo[0][0] = first
    for i in range(1, N):
        each_l = len(memo[i])
        for j in range(each_l):
            if j == 0:
                memo[i][j] = memo[i - 1][j] + triangle[i][j]
            elif j == each_l - 1:
                memo[i][j] = memo[i - 1][j - 1] + triangle[i][j]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - 1]) + triangle[i][j]
        values.extend(memo[i])

    return max(values)
