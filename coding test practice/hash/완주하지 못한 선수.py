"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42576

"""

from collections import Counter


def solution(participant, completion):
    part_count = Counter(participant)
    comp_count = Counter(completion)

    for name, count in part_count.items():
        if count - comp_count[name] == 1:
            return name
