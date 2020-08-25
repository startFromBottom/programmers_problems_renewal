"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42584

"""


def solution(prices):
    ans = [0] * len(prices)
    stack = []  # store (index, price)

    for i, p in enumerate(prices):

        if not stack or stack[-1][1] <= p:
            stack.append((i, p))

        elif stack[-1][1] > p:
            while stack and stack[-1][1] > p:
                v, _ = stack.pop()
                ans[v] = i - v
            stack.append((i, p))

    # Handling remaining elements on the stack
    for each in stack:
        i, v = each
        ans[i] += len(prices) - 1 - i

    return ans
