"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42890?language=python3

"""

from itertools import combinations
from collections import defaultdict


def solution(relation):
    # make all possible cases
    N = len(relation[0])
    cols = [c for c in range(N)]
    all_cases = []

    for i in range(1, N + 1):
        cases = list(combinations(cols, i))
        all_cases.extend(cases)

    # key : column index, value : column values
    col_dict = defaultdict(list)
    for r in relation:
        for i in range(N):
            col_dict[i].append(r[i])

    candidates = set()

    for case in all_cases:
        skip = False
        for cand in candidates:
            # check minimality
            if len(set(cand) & set(case)) == len(cand):
                skip = True
                break
        if skip:  # Minimality does not hold.
            continue
        # make combined columns
        combined_cols = col_dict[case[0]]
        for c in range(1, len(case)):
            combined_cols = [t + d for t, d in zip(combined_cols, col_dict[case[c]])]
        # check Uniqueness
        if len(combined_cols) == len(set(combined_cols)):
            candidates.add(case)

    return len(candidates)
