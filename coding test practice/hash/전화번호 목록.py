"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

"""


def solution(phone_book):
    lengths = [len(p) for p in phone_book]
    min_l = min(lengths)

    min_idxs = set([i for i, l in enumerate(lengths) if l == min_l])
    min_phones = set([phone_book[i] for i in min_idxs])

    for _, phone in enumerate(phone_book):
        for _, m in enumerate(min_phones):
            if phone != m and phone.startswith(m):
                return False

    return True
