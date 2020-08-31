"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

"""

from collections import deque, namedtuple


def check_word_convert(word1: str, word2: str):
    different = 0
    for s1, s2 in zip(word1, word2):
        if s1 != s2:
            different += 1
    return different == 1


def bfs(begin, target, words):
    if target not in words:
        return 0
    Word = namedtuple("Word", "word depth")
    queue = deque([Word(word=begin, depth=0)])
    while queue:
        pop_word = queue.pop()
        current_depth = pop_word.depth
        for word in words:
            if check_word_convert(pop_word.word, word):
                if word == target:
                    return current_depth + 1
                queue.appendleft(Word(word=word, depth=current_depth + 1))
    return 0


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer
