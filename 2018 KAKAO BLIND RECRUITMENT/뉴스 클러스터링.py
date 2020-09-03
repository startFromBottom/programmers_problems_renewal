"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/17677

"""

from collections import Counter


def is_valid(s: str) -> bool:
    for char in s:
        if ord(char) < ord('a') or ord(char) > ord('z'):
            return False
    return True


def solution(str1, str2):
    words1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1)]
    words2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1)]

    words1 = [w for w in words1 if is_valid(w)]
    words2 = [w for w in words2 if is_valid(w)]

    c1, c2 = Counter(words1), Counter(words2)
    s1, s2 = set(words1), set(words2)

    union = s1 | s2
    intersection = s1 & s2

    denom = sum([max(c1[k], c2[k]) for k in union])
    numer = sum([min(c1[k], c2[k]) for k in intersection])

    return int((numer / denom) * 65536) if denom != 0 else 65536
