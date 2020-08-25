"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3#

"""


def solution(progresses, speeds):
    N = len(progresses)

    # step 1 : calculate finish time in each progresses
    finish_days = []
    for p, s in zip(progresses, speeds):
        days = (100 - p) // s + 1
        if (100 - p) % s == 0:
            days -= 1
        finish_days.append(days)

    # step 2 : make answers by using stack
    stack = [finish_days[0]]
    ans = []
    cnt = 1

    for i in range(1, N):
        d = finish_days[i]

        if stack[-1] >= d:
            cnt += 1
        else:
            ans.append(cnt)
            stack.append(d)
            cnt = 1

    ans.append(cnt)

    return ans
