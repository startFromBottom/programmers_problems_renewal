"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42579

"""

from collections import defaultdict
from itertools import chain


def solution(genres, plays):

    # step 1. Make criteria of Condition 1
    genre_sum = defaultdict(int)
    for g, p in zip(genres, plays):
        genre_sum[g] += p

    # step 2. Sort songs by Condition 1, 2, 3
    indexs = range(len(genres))
    infos = [(genre_sum[g], g, p, i) for i, g, p in zip(indexs, genres, plays)]
    infos.sort(key=lambda x: (-x[0], -x[2], x[3]))

    # step 3. Extract top 2 songs in each genres
    genre_top2 = defaultdict(list)
    for info in infos:
        g, idx = info[1], info[-1]
        if len(genre_top2[g]) < 2:
            genre_top2[g].append(info[-1])

    return list(chain(*genre_top2.values()))
