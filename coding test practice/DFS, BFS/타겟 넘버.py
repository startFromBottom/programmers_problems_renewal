"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

"""

cnt = 0


def go(current, idx, numbers, target):
    global cnt

    if idx == len(numbers):
        if current == target:
            cnt += 1
        return

    go(current + numbers[idx], idx + 1, numbers, target)
    go(current - numbers[idx], idx + 1, numbers, target)


def solution(numbers, target):
    go(0, 0, numbers, target)

    return cnt
