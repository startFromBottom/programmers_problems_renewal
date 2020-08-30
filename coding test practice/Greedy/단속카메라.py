"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42884

"""


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0], x[1]))

    stack = [routes[0]]
    for i in range(1, len(routes)):

        last_start, last_end = stack[-1]
        start, end = routes[i]

        if start > last_end:
            stack.append(routes[i])
        else:
            new_start = max(start, last_start)
            new_end = min(end, last_end)
            stack[-1] = [new_start, new_end]

    return len(stack)
