"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3#

"""


def solution(number, k):
    L = len(number)
    s = L - k  # 뽑아야하는 수의 개수
    cnt = 0
    stack = []

    for i, char in enumerate(number):
        if (not stack or stack[-1] >= char) and cnt < s:
            stack.append(char)
            cnt += 1
            continue
        while stack and stack[-1] < char and s - cnt < L - i:
            stack.pop()
            cnt -= 1
        if cnt < s:
            stack.append(char)
            cnt += 1

    return "".join(stack)
