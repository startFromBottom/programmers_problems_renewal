"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

"""

from collections import defaultdict


def solution(clothes):
    cloth_cat = defaultdict(list)

    for cloth, cat in clothes:
        cloth_cat[cat].append(cloth)

    ans = 1
    for cat, cloth in cloth_cat.items():
        ans *= (len(cloth) + 1)
    return ans - 1
