"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

"""


def solution(array, commands):
    answer = []
    for command in commands:
        start, end, index = command
        sliced_array = array[start - 1:end]
        sliced_array.sort()
        answer.append(sliced_array[index - 1])

    return answer
